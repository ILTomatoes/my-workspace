# 工作空间共享 Skills

在这里维护可跨项目复用的技能源，每项使用 `skills/<name>/SKILL.md`，配套脚本、模板和示例放在同一目录。此目录纳入工作空间 Git，可随 clone / pull 带到其他机器。

这是本工作空间共享的技能集合，不会自动写入机器级用户目录，也不会自动启用全部技能。需要某项技能时，由 Agent 读取对应 SKILL.md；需要宿主原生发现或安装时，再为该宿主配置入口。只维护一份源，避免不同工具版本分叉。

新增技能时，在下面登记名称、用途和源文件路径。优先从多次使用的成熟做法提炼，不预先堆积空技能。

以现有源码讲解、AI 分析笔记为材料的专题学习，可先阅读 ai-coding-practice 对应主题；不必为单次阅读初始化学科或建立额外追踪器。希望持续辅导和练习时，再按下面的技能路由组织学科。

## 工作空间同步

[workspace-git-sync](workspace-git-sync/SKILL.md) 提供父仓库与清单仓库的快进同步、异常汇总，以及按当前任务范围审查提交和推送的建议。用户提出“同步仓库”“拉取最新”“推送”时加载此技能。实现入口为 `scripts/workspace-git-sync.py`，不自动提交或推送，也不自动安装到宿主。

## 已登记的学习技能

这些技能的维护源位于独立技能市场仓库，本目录登记引用，不再复制一份。路径以 config/repos.json 中的仓库位置为准；下表使用当前默认布局。

| 技能 | 适用请求 | 维护源入口 | 学习内容归属 |
|---|---|---|---|
| learning-tutor | 持续学科辅导、练习、调试与复习 | repos/projects/my-skills-market/plugins/learning-tutor/skills/learning-tutor/SKILL.md | repos/learning/personal-study-project/<学科>/ |
| ispm-exam-coach | 软考高项应试规划、资料消化、模考反馈 | repos/projects/my-skills-market/plugins/ispm-exam-coach/skills/ispm-exam-coach/SKILL.md | repos/learning/my-exam-gaoxiang/ |

系统架构设计师考试资料与备考记录归入 `repos/learning/my-exam-sa/`。当前未登记该考试的专属教练技能，不直接套用高项的 ispm-exam-coach；普通概念讲解可按需使用 learning-tutor，记录位置和流程遵循考试仓库的实际约定。

Agent 应先加载市场源入口，只按需读取配套 references/ 和脚本。市场源缺失时，learning-tutor 可使用 personal-study-project/.claude/skills/learning-tutor/SKILL.md，考试教练也可使用该仓库内的 .claude/skills/ispm-exam-coach/SKILL.md；说明实际使用位置，不把不同副本同时加载。副本可能落后于市场源，以实际读取的文件为准。

在新机器上，通用学习通常需要先运行：

```bash
python3 scripts/setup.py
python3 scripts/repos.py clone my-skills-market personal-study-project
# 按目标考试克隆需要的资料仓库：
python3 scripts/repos.py clone my-exam-gaoxiang
python3 scripts/repos.py clone my-exam-sa
```

若宿主不自动读取 AGENTS.md / CLAUDE.md，启动任务时显式要求它先读根目录 AGENTS.md。这里提供文件级路由，不保证各宿主自动注册原生技能命令。

根目录 `.claude/skills/` 中已有的标书技能仍作为本地历史内容保留，尚未审查迁入共享集合；迁入前需核实来源、授权、依赖和是否包含本机配置。
