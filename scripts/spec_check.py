#!/usr/bin/env python3
import re
from pathlib import Path
import sys


def find_referenced_files(md_path: Path):
    text = md_path.read_text(encoding='utf-8')
    tests = set(re.findall(r"\btests/[\w\-./]+\.py\b", text))
    skills = set(re.findall(r"\bskills/[\w\-./]+\.py\b", text))
    return tests, skills


def list_fs_files(base: Path, sub: str):
    p = base / sub
    if not p.exists():
        return set()
    return set(str(x.relative_to(base)) for x in p.rglob('*.py'))


def main():
    repo = Path(__file__).resolve().parents[1]
    spec = repo / 'specs' / 'technical.md'
    if not spec.exists():
        print(f"Spec file not found: {spec}")
        sys.exit(2)

    tests_ref, skills_ref = find_referenced_files(spec)
    tests_fs = list_fs_files(repo, 'tests')
    skills_fs = list_fs_files(repo, 'skills')

    ok = True

    if tests_ref:
        missing = tests_ref - tests_fs
        if missing:
            print("Missing test files referenced in specs:")
            for m in sorted(missing):
                print(" -", m)
            ok = False
        else:
            print("All referenced test files present")
    else:
        print("No test file references found in specs/technical.md")

    if skills_ref:
        missing = skills_ref - skills_fs
        if missing:
            print("Missing skills files referenced in specs:")
            for m in sorted(missing):
                print(" -", m)
            ok = False
        else:
            print("All referenced skills files present")
    else:
        print("No skills file references found in specs/technical.md")

    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
