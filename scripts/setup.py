#!/usr/bin/env python3
"""Create local workspace directories without fetching or changing repositories."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    for relative in (
        "repos/notes", "repos/projects", "repos/learning",
        "references/opensource-code-pro", "local", "outputs", "tmp",
    ):
        (ROOT / relative).mkdir(parents=True, exist_ok=True)
    print(f"Initialized local directories in {ROOT}")
    print("Shared guidance: AGENTS.md, knowledge/README.md, skills/README.md")
    print("List repositories: python3 scripts/repos.py list")
    print("Clone selected repositories: python3 scripts/repos.py clone <name> ...")
