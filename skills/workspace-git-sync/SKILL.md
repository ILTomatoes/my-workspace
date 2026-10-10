---
name: workspace-git-sync
description: 同步 my-workspace 及清单中的独立仓库，快进拉取并汇总改动、分叉和待推送状态；用户要求提交推送时审查指定范围并分别交付。
---

# 工作空间 Git 同步

在 my-workspace 根目录操作，先读 AGENTS.md。实际仓库集来自 config/repos.json 和可选 config/repos.local.json；父仓库使用名称 workspace。不存在的仓库报告缺失，不隐式克隆。

## 拉取更新

用户要求“同步仓库”“拉取最新”或“更新所有仓库”时运行：

```bash
python3 scripts/workspace-git-sync.py
# 指定仓库
python3 scripts/workspace-git-sync.py workspace my-exam-sa
# 本地预览，不访问远端
python3 scripts/workspace-git-sync.py --dry-run
# 需要清理失效分支时
python3 scripts/workspace-git-sync.py --prune-merged
```

脚本对干净工作树使用当前分支的真实 upstream，fetch --prune 后仅快进更新；跳过有改动、分叉、缺失或上游异常的仓库。本地领先仅报告待推送。默认不删除本地分支；--prune-merged 仅尝试用 branch -d 删除上游已消失且已合并到当前 HEAD 的分支。

预览只说明当前本地条件，不证明远端同步。脚本返回非零时逐项解释未完成原因，不把部分成功报告为全部完成。

## 提交与推送

“推送”按当前任务明确涉及的仓库处理；只有用户明确要求整个空间时才扩大范围。同步脚本不自动提交或推送。

先检查目标仓库的状态、diff、未跟踪文件及自身约定，区分本次内容与已有工作。使用明确路径暂存并审查 staged diff，运行适合变更的检查，再分别提交。用户要求整体 clean 时也先审查既有内容；不能用丢弃改动、隐式 stash 或新增忽略规则掩盖未处理工作。

核实当前分支、upstream 和推送地址，不固定 main 或 origin；无上游时说明目标，不擅自选择新远端。fetch 后无分叉可快进；分叉、冲突或远端拒绝时保留现场并报告，不强推、reset 或自动 rebase。发布仓库 main 推送会触发 GitHub Pages，执行前说明实际效果。

结束时逐仓库报告提交、推送和 clean 状态，并核实 HEAD 与实际远端目标一致。父仓库干净不能代表子仓库干净；忽略的本地配置不属于 Git clean 检查。保留未授权或未审查的内容，并明确列出剩余项。
