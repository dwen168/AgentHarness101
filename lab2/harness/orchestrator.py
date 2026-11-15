from dataclasses import asdict
 
from harness.config import HarnessConfig
from harness.context import collect_repository_context
from harness.executor import execute_agent
from harness.logger import HarnessLogger
from harness.planner import create_plan
from harness.verifier import verify_changes
 
 
def request_human_approval(plan: dict) -> bool:
    print("\nProposed Plan")

    for key, value in plan.items():
        print(f"{key}: {value}")

    answer = input("\nApprove execution? Type yes to continue: ")

    return answer.strip().lower() == "yes"


class AIHarness:
    def __init__(self, config: HarnessConfig) -> None:
        self.config = config
        self.logger = HarnessLogger(config.log_directory)
 
    def run(self, task: str) -> bool:
        self.logger.log(
            "task_received",
            {"task": task},
        )
 
        if not task.strip():
            self.logger.log(
                "task_rejected",
                {"reason": "Task cannot be empty"},
            )
            return False
 
        repository_context = collect_repository_context(
            self.config.project_path
        )
 
        self.logger.log(
            "context_collected",
            {
                "characters": len(repository_context),
                "project_path": str(self.config.project_path),
            },
        )
 
        plan = create_plan(task, repository_context)
        plan_data = asdict(plan)

        self.logger.log(
            "plan_created",
            plan_data,
        )

        if not request_human_approval(plan_data):
            self.logger.log(
                "workflow_cancelled",
                {"reason": "Human approval denied"},
            )
            return False
 
        for attempt in range(1, self.config.max_retries + 2):
            self.logger.log(
                "execution_started",
                {
                    "attempt": attempt,
                    "agent": self.config.agent_command,
                },
            )
 
            execution_result = execute_agent(
                agent_command=self.config.agent_command,
                project_path=self.config.project_path,
                task=task,
                timeout_seconds=self.config.timeout_seconds,
            )
 
            self.logger.log(
                "execution_completed",
                {
                    "attempt": attempt,
                    "success": execution_result.success,
                    "stdout": execution_result.stdout,
                    "stderr": execution_result.stderr,
                    "return_code": execution_result.return_code,
                },
            )
 
            verification_result = verify_changes(
                project_path=self.config.project_path,
                test_command=self.config.test_command,
                timeout_seconds=self.config.timeout_seconds,
            )
 
            self.logger.log(
                "verification_completed",
                {
                    "attempt": attempt,
                    "passed": verification_result.passed,
                    "checks": verification_result.checks,
                    "test_stdout": verification_result.test_result.stdout,
                    "test_stderr": verification_result.test_result.stderr,
                },
            )
 
            if verification_result.passed:
                self.logger.log(
                    "workflow_completed",
                    {
                        "status": "success",
                        "attempts": attempt,
                    },
                )
                return True
 
            if attempt <= self.config.max_retries:
                self.logger.log(
                    "retry_scheduled",
                    {
                        "next_attempt": attempt + 1,
                        "reason": "Verification failed",
                    },
                )
 
        self.logger.log(
            "workflow_completed",
            {
                "status": "failure",
                "reason": "Maximum retries exceeded",
            },
        )
 
        return False