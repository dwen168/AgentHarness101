from dataclasses import dataclass
from pathlib import Path
 
from harness.executor import ExecutionResult, run_command
 
 
@dataclass
class VerificationResult:
    passed: bool
    test_result: ExecutionResult
    checks: list[str]
 
 
def verify_changes(
    project_path: Path,
    test_command: tuple[str, ...],
    timeout_seconds: int,
) -> VerificationResult:
    checks: list[str] = []
 
    test_result = run_command(
        command=list(test_command),
        working_directory=project_path,
        timeout_seconds=timeout_seconds,
    )
 
    if test_result.success:
        checks.append("Test suite passed")
    else:
        checks.append("Test suite failed")
 
    calculator_file = project_path / "calculator.py"
    test_file = project_path / "test_calculator.py"
 
    calculator_content = calculator_file.read_text(encoding="utf-8")
    test_content = test_file.read_text(encoding="utf-8")
 
    has_zero_check = "if b == 0" in calculator_content
    has_new_test = "test_divide_by_zero" in test_content
 
    checks.append(
        "Division-by-zero guard found"
        if has_zero_check
        else "Division-by-zero guard missing"
    )
 
    checks.append(
        "Division-by-zero test found"
        if has_new_test
        else "Division-by-zero test missing"
    )
 
    passed = (
        test_result.success
        and has_zero_check
        and has_new_test
    )
 
    return VerificationResult(
        passed=passed,
        test_result=test_result,
        checks=checks,
    )