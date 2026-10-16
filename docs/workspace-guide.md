# 使用与维护

日常任务的仓库选择与写入建议见 [仓库索引](repositories.md) 和 [Agent 使用指南](agent-guide.md)。

## 新机器恢复

1. 克隆 `https://github.com/ILTomatoes/my-workspace.git`。
2. 运行 `python3 scripts/setup.py` 创建本地目录，再运行 `python3 scripts/repos.py list` 查看清单。
3. 运行 `python3 scripts/repos.py clone <name> ...` 克隆需要的仓库，或 `python3 scripts/repos.py clone --all` 克隆全部登记仓库。已有路径会跳过，不更新或覆盖。
4. 从自己的安全备份恢复 `config/repos.local.json`、私有笔记库和本地配置。工作空间不会备份这些被忽略的内容。

## 纳入一个仓库

根据用途放入 `repos/notes/`、`repos/projects/` 或 `repos/learning/`。已有仓库移动整个目录，包括 `.git` 和隐藏文件；新仓库直接克隆。

在 `config/repos.json` 中追加记录：`name` 是唯一名称，`path` 是工作空间相对路径，`url` 是无凭证的远程地址，`purpose` 描述用途。`url` 留空表示尚未登记远端或只在本地维护，这类条目不参与 `clone` 和同步，需要时补上地址。

不希望公开名称和地址的仓库，只在 `config/repos.local.json` 添加记录。两份清单里的 name 和 path 不应重复。两个 Obsidian 库已登记在 config/repos.json，可用 `python3 scripts/repos.py clone my-obsidian-notes my-obsidian-knowledge-base` 恢复到本地。

同时更新 [docs/repositories.md](repositories.md) 的用途、读取入口和写入建议，再运行 `python3 scripts/repos.py list` 检查清单能否正确加载，并用 `git check-ignore repos/<分类>/<name>/` 确认独立仓库受到忽略规则保护。

运行 `python3 scripts/repos.py status` 检查当前分支和改动。工具只读取状态，不自动拉取、重置、提交或推送；需要同步时进入相应仓库执行 Git 操作。

## 记录工作

短任务直接完成，不强制创建文档。有持续价值的记录才落盘：

- journal/：当天完成了什么、得到什么结论、下一步是什么。
- plans/：目标、范围、阶段和验收；业余项目也从这里起步。
- learning/：跨主题技术总结；专题分析学习归 ai-coding-practice，持续学科会话、练习和进度归 personal-study-project。
- references/：来源链接、阅读索引和个人提炼；原始下载内容放本地参考目录。

工作项目笔记与日志归属 my-obsidian-notes，长期知识卡片归属 my-obsidian-knowledge-base；文章视频收录归属 my-daily-remarks，公开文章归属 my-ai-observe-notes。项目自身资料归属项目仓库，工作空间保留跨项目的入口和总结，避免重复维护正文。

## 同步

按 [workspace-git-sync](../skills/workspace-git-sync/SKILL.md) 操作。`python3 scripts/workspace-git-sync.py` 同步父仓库及公共/本地清单仓库，也可指定名称；workspace 表示父仓库。使用 `--dry-run` 仅检查本地条件，使用 `--prune-merged` 清理已合并且上游已消失的本地分支。存在跳过、异常或待推送项时返回非零，具体情况见逐仓库汇总。

脚本不 stash、reset、rebase、强推或自动提交；有本地工作先保留并说明，按任务授权处理后再同步。它不会扫描清单外的参考源码。

## 提交与备份

在工作空间根目录审查 `git status` 和 `git diff --cached`，只添加管理文件和准备分享的记录。独立仓库进入其目录单独提交。

`repos/`、本地清单、参考源码、local/ 和运行产物均被忽略；需要独立备份或推送到各自的私有远程。`.claude/` 中原有技能和本地设置已保留，当前按本地配置处理，后续审查后再决定哪些通用技能纳入版本管理。

移动后，编辑器最近项目、Obsidian 打开路径、运行中的终端和旧脚本可能仍引用旧路径，需要更新或重新打开。不会自动改写子仓库内部内容。

## 在另一台机器继续工作

首次使用：

```bash
git clone https://github.com/ILTomatoes/my-workspace.git
cd my-workspace
python3 scripts/setup.py
python3 scripts/repos.py clone my-skills-market
```

后续更新工作空间时先检查本地改动，再 `git pull --ff-only`。这会更新共享技能源、知识、清单和管理文件，独立仓库仍需各自同步。若新增本地目录，可再次运行 setup.py。

共享技能在 skills/，全局知识在 knowledge/。Agent 的加载入口是 AGENTS.md；只按任务读取需要的条目。已有 .claude/skills/ 仍为本地历史技能，尚未迁入共享源。公共清单会随工作空间同步，本地清单不会；选择放入哪一份时，以信息是否适合随本仓库分享为准。
