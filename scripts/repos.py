#!/usr/bin/env python3
"""List, inspect, or explicitly clone independent workspace repositories."""

import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def load_repos():
    repos = []
    names, paths = set(), set()
    for filename in ("repos.json", "repos.local.json"):
        source = ROOT / "config" / filename
        if filename == "repos.local.json" and not source.exists():
            continue
        data = json.loads(source.read_text(encoding="utf-8"))
        for repo in data["repos"]:
            for key in ("name", "path", "url", "purpose"):
                if not isinstance(repo.get(key), str) or not repo[key].strip():
                    raise ValueError(f"{filename}: missing or invalid {key}")
            relative = Path(repo["path"])
            target = (ROOT / relative).resolve()
            if relative.is_absolute() or ".." in relative.parts or not target.is_relative_to(ROOT / "repos"):
                raise ValueError(f"{filename}: path must be inside repos/: {relative}")
            if repo["name"] in names or target in paths:
                raise ValueError(f"{filename}: duplicate name or path: {repo['name']}")
            names.add(repo["name"])
            paths.add(target)
            repos.append(repo)
    return repos


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("list", "status", "clone"))
    parser.add_argument("names", nargs="*", help="Repository names to clone")
    parser.add_argument("--all", action="store_true", help="Clone all registered repositories")
    args = parser.parse_args()
    try:
        repos = load_repos()
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"Registry error: {error}\n")
    if args.command == "clone":
        if bool(args.names) == args.all:
            parser.error("clone requires repository names or --all")
        unknown = set(args.names) - {repo["name"] for repo in repos}
        if unknown:
            parser.error(f"Unknown repositories: {', '.join(sorted(unknown))}")
        repos = [repo for repo in repos if args.all or repo["name"] in args.names]
    elif args.names or args.all:
        parser.error("names and --all apply only to clone")
    failed = False
    for repo in repos:
        print(f"{repo['name']}  [{repo['path']}]", flush=True)
        if args.command == "list":
            print(f"  {repo['purpose']}\n  {repo['url']}")
            continue
        target = ROOT / repo["path"]
        if args.command == "clone":
            if target.exists():
                print("  SKIPPED: path already exists; inspect it with status")
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            result = subprocess.run(["git", "clone", "--", repo["url"], str(target)], check=False)
            failed |= result.returncode != 0
            continue
        if not (target / ".git").exists():
            print("  MISSING: repository has not been cloned here")
            failed = True
            continue
        result = subprocess.run(
            ["git", "--no-optional-locks", "-C", str(target), "status", "--short", "--branch"],
            capture_output=True, text=True, check=False,
        )
        for line in (result.stdout or result.stderr).splitlines():
            print(f"  {line}")
        failed |= result.returncode != 0
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
