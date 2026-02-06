"""Minimal trend_fetcher stub for TDD progression."""
from typing import Dict, Any


def fetch_trends() -> Dict[str, Any]:
    """Return a dummy trends payload conforming to Agent Task expectations."""
    return {
        "id": "22222222-2222-2222-2222-222222222222",
        "task_type": "analyze_video",
        "payload": {"video_url": "https://example.com/dummy.mp4"},
        "created_at": "2026-02-06T00:00:00Z"
    }
