import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
 
 
class HarnessLogger:
    def __init__(self, log_directory: Path) -> None:
        self.log_directory = log_directory
        self.log_directory.mkdir(parents=True, exist_ok=True)
 
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_directory / f"harness_{timestamp}.jsonl"
 
    def log(self, event: str, data: dict[str, Any]) -> None:
        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "data": data,
        }
 
        with self.log_file.open("a", encoding="utf-8") as file:
            file.write(json.dumps(record) + "\n")
 
        print(f"[{event}] {data}")