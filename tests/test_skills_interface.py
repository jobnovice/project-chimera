import pytest

# Intentionally import the unimplemented skills interface to produce a failing test
import skills.skills_interface  # type: ignore

from tests.helpers.schema_validator import load_and_validate_example


def test_skills_output_contract():
    # Minimal example representing a skills response that would be persisted to video_metadata
    example = {
        "id": "11111111-1111-1111-1111-111111111111",
        "task_type": "generate_caption",
        "payload": {"video_url": "https://example.com/video2.mp4"},
        "created_at": "2026-02-06T00:00:00Z"
    }

    load_and_validate_example('Agent Task', example)
