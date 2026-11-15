from dataclasses import dataclass
from pathlib import Path
 
 
@dataclass(frozen=True)
class HarnessConfig:
    project_path: Path
    log_directory: Path
    max_retries: int = 2
    timeout_seconds: int = 120
    agent_command: str = "simulate"
    test_command: tuple[str, ...] = ("pytest", "-v")