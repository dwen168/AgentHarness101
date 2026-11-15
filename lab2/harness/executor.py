import subprocess
from dataclasses import dataclass
from pathlib import Path
 
 
BLOCKED_COMMAND_PATTERNS = {
    "rm -rf",
    "format ",
    "shutdown",
    "reboot",
    "del /s",
    "drop database",
}
 
 
@dataclass
class ExecutionResult:
    success: bool
    stdout: str
    stderr: str
    return_code: int
 
 
def is_command_safe(command: str) -> bool:
    normalized = command.lower().strip()
 
    return not any(
        blocked_pattern in normalized
        for blocked_pattern in BLOCKED_COMMAND_PATTERNS
    )
 
 
def run_command(
    command: list[str],
    working_directory: Path,
    timeout_seconds: int,
) -> ExecutionResult:
    command_text = " ".join(command)
 
    if not is_command_safe(command_text):
        return ExecutionResult(
            success=False,
            stdout="",
            stderr=f"Blocked unsafe command: {command_text}",
            return_code=1,
        )
 
    try:
        completed = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
 
        return ExecutionResult(
            success=completed.returncode == 0,
            stdout=completed.stdout,
            stderr=completed.stderr,
            return_code=completed.returncode,
        )
 
    except subprocess.TimeoutExpired as error:
        return ExecutionResult(
            success=False,
            stdout=error.stdout or "",
            stderr="Command timed out",
            return_code=124,
        )

def simulate_agent_execution(project_path: Path, task: str) -> ExecutionResult:
    calculator_file = project_path / "calculator.py"
    test_file = project_path / "test_calculator.py"
 
    if "division" not in task.lower() and "divide" not in task.lower():
        return ExecutionResult(
            success=False,
            stdout="",
            stderr="The simulated agent only supports the division task.",
            return_code=1,
        )
 
    calculator_code = calculator_file.read_text(encoding="utf-8")
 
    old_function = """def divide(a: float, b: float) -> float:
    return a / b
"""
 
    new_function = """def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
 
    return a / b
"""
 
    if old_function not in calculator_code:
        return ExecutionResult(
            success=False,
            stdout="",
            stderr="Expected divide function was not found.",
            return_code=1,
        )
 
    calculator_file.write_text(
        calculator_code.replace(old_function, new_function),
        encoding="utf-8",
    )
 
    test_code = test_file.read_text(encoding="utf-8")
 
    new_test = """
 
def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
"""
 
    if "test_divide_by_zero" not in test_code:
        test_file.write_text(
            test_code + new_test,
            encoding="utf-8",
        )
 
    return ExecutionResult(
        success=True,
        stdout=(
            "Updated calculator.py with division-by-zero handling.\n"
            "Added a division-by-zero test."
        ),
        stderr="",
        return_code=0,
    )

def run_external_agent(
    agent_command: str,
    project_path: Path,
    task: str,
    timeout_seconds: int,
) -> ExecutionResult:
    prompt = (
        "You are operating inside a controlled coding harness.\n\n"
        f"Task:\n{task}\n\n"
        "Requirements:\n"
        "- Make the smallest safe change.\n"
        "- Add or update tests.\n"
        "- Do not modify unrelated files.\n"
        "- Do not install new dependencies.\n"
        "- Do not run destructive commands.\n"
        "- Summarize the files changed.\n"
    )
 
    if agent_command == "claude":
        command = ["claude", "-p", prompt]
    elif agent_command == "codex":
        command = ["codex", "exec", prompt]
    elif agent_command == "gemini":
        command = ["gemini", "-p", prompt]
    else:
        return ExecutionResult(
            success=False,
            stdout="",
            stderr=f"Unsupported agent command: {agent_command}",
            return_code=1,
        )
 
    return run_command(
        command=command,
        working_directory=project_path,
        timeout_seconds=timeout_seconds,
    )

def execute_agent(
    agent_command: str,
    project_path: Path,
    task: str,
    timeout_seconds: int,
) -> ExecutionResult:
    if agent_command == "simulate":
        return simulate_agent_execution(project_path, task)
 
    return run_external_agent(
        agent_command=agent_command,
        project_path=project_path,
        task=task,
        timeout_seconds=timeout_seconds,
    )