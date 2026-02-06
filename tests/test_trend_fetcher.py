import pytest

# Attempt to import the (not-yet-implemented) trend_fetcher module from skills.
# This import is intentionally unimplemented to produce a failing (red) test state
# as required by our TDD workflow.
import skills.trend_fetcher  # type: ignore

from tests.helpers.schema_validator import load_and_validate_example


def test_trend_payload_matches_agent_task_schema():
    # This example is deliberately minimal — schema validation focuses on required keys.
    example = {
        "id": "00000000-0000-0000-0000-000000000000",
        "task_type": "analyze_video",
        "payload": {"video_url": "https://example.com/video.mp4"},
        "created_at": "2026-02-06T00:00:00Z"
    }

    # Validate against the `Agent Task` schema embedded in specs/technical.md
    load_and_validate_example('Agent Task', example)
