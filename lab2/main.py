from pathlib import Path
 
from harness.config import HarnessConfig
from harness.orchestrator import AIHarness
 
 
def main() -> None:
    project_path = Path("sample_project").resolve()
    log_directory = Path("logs").resolve()
 
    config = HarnessConfig(
        project_path=project_path,
        log_directory=log_directory,
        max_retries=2,
        timeout_seconds=120,
        agent_command="simulate",
        test_command=("pytest", "-v"),
    )
 
    harness = AIHarness(config)
 
    task = (
        "Update the divide function so division by zero raises "
        "a clear ValueError, and add a test for the behavior."
    )
 
    success = harness.run(task)
 
    if success:
        print("\nHarness completed successfully.")
    else:
        print("\nHarness failed.")
 
 
if __name__ == "__main__":
    main()