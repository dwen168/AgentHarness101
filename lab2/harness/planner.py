from dataclasses import dataclass
 
 
@dataclass
class ExecutionPlan:
    objective: str
    files_to_inspect: list[str]
    expected_changes: list[str]
    verification_steps: list[str]
 
 
def create_plan(task: str, repository_context: str) -> ExecutionPlan:
    context_lower = repository_context.lower()
    task_lower = task.lower()
 
    files_to_inspect: list[str] = []
    expected_changes: list[str] = []
    verification_steps: list[str] = ["Run the complete test suite"]
 
    if "divide" in task_lower or "division" in task_lower:
        if "calculator.py" in context_lower:
            files_to_inspect.append("calculator.py")
 
        if "test_calculator.py" in context_lower:
            files_to_inspect.append("test_calculator.py")
 
        expected_changes.extend(
            [
                "Add explicit division-by-zero handling",
                "Add a test for division by zero",
                "Preserve existing calculator behavior",
            ]
        )
 
    if not files_to_inspect:
        files_to_inspect.append("Inspect all relevant source files")
 
    if not expected_changes:
        expected_changes.append("Make the smallest safe change")
 
    return ExecutionPlan(
        objective=task,
        files_to_inspect=files_to_inspect,
        expected_changes=expected_changes,
        verification_steps=verification_steps,
    )