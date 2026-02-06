import json
from pathlib import Path
from typing import Dict, Any


def load_json_schemas_from_markdown(md_path: str) -> Dict[str, Dict[str, Any]]:
    """Extract JSON blocks from a markdown file and return a map by schema title."""
    p = Path(md_path)
    text = p.read_text(encoding="utf-8")
    schemas = {}
    in_block = False
    buf = []
    for line in text.splitlines():
        if line.strip().startswith('```json'):
            in_block = True
            buf = []
            continue
        if in_block and line.strip().startswith('```'):
            in_block = False
            try:
                obj = json.loads('\n'.join(buf))
                title = obj.get('title') or obj.get('$id') or obj.get('name')
                if title:
                    schemas[title] = obj
            except Exception:
                # skip non-json blocks
                pass
            buf = []
            continue
        if in_block:
            buf.append(line)
    return schemas


def validate_required_keys(instance: Dict[str, Any], schema: Dict[str, Any]):
    """Lightweight validator: ensure required top-level keys exist."""
    required = schema.get('required') or []
    missing = [k for k in required if k not in instance]
    if missing:
        raise AssertionError(f"Missing required keys: {missing}")


def load_and_validate_example(schema_title: str, example: Dict[str, Any]):
    base = Path(__file__).resolve().parents[2]
    spec = base / 'specs' / 'technical.md'
    schemas = load_json_schemas_from_markdown(str(spec))
    if schema_title not in schemas:
        raise KeyError(f"Schema '{schema_title}' not found in {spec}")
    validate_required_keys(example, schemas[schema_title])
