#!/usr/bin/env python3
"""Fast-forward workspace repositories using their configured upstreams."""

import argparse
from collections import Counter
from pathlib import Path
import subprocess

from repos import ROOT, load_repos


def git(path, *args):
    result = subprocess.run(
        ["git", "-C", str(path), *args], capture_output=True, text=True,
    )
    if result.returncode:
        raise RuntimeError((result.stderr or result.stdout).strip())
    return result.stdout.strip()


def sync_repo(path, expected_url=None, dry_run=False, prune_merged=False):
    if not path.exists():
        return "跳过", "尚未克隆"
    try:
        if Path(git(path, "rev-parse", "--show-toplevel")).resolve() != path.resolve():
            return "跳过", "路径不是独立仓库根目录"
        if git(path, "status", "--porcelain"):
            return "跳过", "工作树有改动，保留现场"
        branch = git(path, "symbolic-ref", "--quiet", "--short", "HEAD")
        upstream = git(path, "rev-parse", "--abbrev-ref", "@{upstream}")
        remote = git(path, "config", "--get", f"branch.{branch}.remote")
        if remote == ".":
            return "跳过", "上游是本地分支"
        if expected_url and git(path, "remote", "get-url", remote) != expected_url:
            return "跳过", "上游远端与清单地址不一致"
        if dry_run:
            return "预览", f"{branch} ← {upstream}；将 fetch --prune 并仅快进更新"
        before = git(path, "rev-parse", "HEAD")
        git(path, "fetch", "--prune", remote)
        ahead, behind = map(int, git(path, "rev-list", "--left-right", "--count", "HEAD...@{upstream}").split())
        if ahead and behind:
            return "跳过", f"分支已分叉：本地领先 {ahead}，落后 {behind}"
        if ahead:
            return "待推送", f"本地领先 {ahead} 个提交；同步脚本不推送"
        if behind:
            git(path, "merge", "--ff-only", "@{upstream}")
        deleted, retained = [], []
        if prune_merged:
            refs = git(path, "for-each-ref", "--format=%(refname:short)|%(upstream)|%(upstream:track)", "refs/heads")
            for line in refs.splitlines():
                name, tracking, state = line.split("|", 2)
                if name == branch or not tracking.startswith(f"refs/remotes/{remote}/") or state != "[gone]":
                    continue
                # Require merge into current HEAD, not only the deleted upstream.
                result = subprocess.run(["git", "-C", str(path), "merge-base", "--is-ancestor", name, "HEAD"], capture_output=True)
                if result.returncode:
                    retained.append(name)
                    continue
                try:
                    git(path, "branch", "-d", "--", name)
                    deleted.append(name)
                except RuntimeError:
                    retained.append(name)
        note = f"快进 {behind} 个提交" if before != git(path, "rev-parse", "HEAD") else "与上游一致"
        if deleted:
            note += "; 已删除已合并的失效分支：" + ", ".join(deleted)
        if retained:
            note += "; 保留分支：" + ", ".join(retained)
        if git(path, "status", "--porcelain"):
            return "异常", "更新后工作树有改动，请检查"
        return "更新" if behind else "最新", note
    except (RuntimeError, ValueError, OSError) as error:
        # Git output can include configured URLs; avoid exposing credentials.
        return "异常", f"Git 操作未完成（{type(error).__name__}）；请在目标仓库检查分支、上游与访问权限"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", help="清单中的名称；workspace 表示父仓库，默认全部")
    parser.add_argument("--dry-run", action="store_true", help="只检查本地，不连接远端或修改引用")
    parser.add_argument("--prune-merged", action="store_true", help="删除上游已消失且已合并到当前 HEAD 的本地分支")
    args = parser.parse_args()
    try:
        entries = {"workspace": (ROOT, None)}
        for repo in load_repos():
            if repo["name"] == "workspace":
                raise ValueError("workspace 是父仓库的保留名称")
            entries[repo["name"]] = (ROOT / repo["path"], repo["url"])
    except (OSError, ValueError, KeyError, TypeError):
        parser.exit(2, "仓库清单无法加载，请检查字段、重复名称和路径\n")
    unknown = set(args.names) - entries.keys()
    if unknown:
        parser.error("未知仓库：" + ", ".join(sorted(unknown)))
    counts = Counter()
    for name in dict.fromkeys(args.names or entries):
        path, url = entries[name]
        if name != "workspace" and not (url or "").strip():
            state, note = "跳过", "清单未登记远端地址"
        else:
            state, note = sync_repo(path, url, args.dry_run, args.prune_merged)
        counts[state] += 1
        print(f"{name}: {state} — {note}", flush=True)
    print("汇总：" + " / ".join(f"{state} {count}" for state, count in counts.items()))
    return int(bool(counts["跳过"] or counts["异常"] or counts["待推送"]))


if __name__ == "__main__":
    raise SystemExit(main())
