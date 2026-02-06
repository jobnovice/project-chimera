"""Minimal skills_interface stub for TDD progression."""
from typing import Dict, Any


def handle_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Accept a task dict and return a dummy success result.

    This keeps behavior simple for tests and will be expanded later.
    """
    return {
        "task_id": task.get("id"),
        "status": "succeeded",
        "result": {"message": "stub executed"},
        "confidence": 1.0,
    }
