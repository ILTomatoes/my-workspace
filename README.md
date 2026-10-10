# my-workspace

个人学习与工作的总入口：组织独立仓库，连接学习资料、练习进度、工作笔记与公开输出，记录计划和可复用经验。

借鉴 aip-workspace 的「工作空间 + 独立仓库 + 仓库清单」方式，先保持轻量；具体源码、完整笔记和项目历史留在各自仓库。

## 给日常任务和 Agent 的入口

这个工作空间也可作为 Hermes Agent 等助手的任务根目录：查询已有资料、整理日常收录、修改项目内容、维护计划与跨项目知识。内容的实际归属由仓库清单和目标仓库约定决定。

- 协作规则：[AGENTS.md](AGENTS.md)。
- 按任务选择仓库：[仓库索引](docs/repositories.md)；名称、路径与远端以 [config/repos.json](config/repos.json) 和可选本地清单为准。
- 查询、写入、归档和交接：[Agent 使用指南](docs/agent-guide.md)。
- 克隆、同步与新增仓库：[使用与维护](docs/workspace-guide.md)。

通常从任务相关的索引、README 和近期内容开始读。清单表示“已登记”，不代表当前机器已克隆；本地状态通过 `python3 scripts/repos.py status` 查看。

## 目录

```text
my-workspace/
├── AGENTS.md / CLAUDE.md    # AI 协作入口
├── config/                 # 仓库清单
├── scripts/                # 初始化和仓库管理工具
├── skills/                 # 跨项目共享技能源，随 Git 同步
├── knowledge/              # 全局知识与可复用经验，随 Git 同步
├── docs/                   # 工作空间使用说明和整理记录
├── plans/                  # 个人规划、业余项目想法
├── journal/                # 日常工作记录、周/月复盘
├── learning/               # 跨仓库的技术学习总结
├── templates/              # 记录模板
├── repos/                  # 独立 Git 仓库，本地目录
│   ├── notes/              # Obsidian 笔记库、日常收录、笔记发布站
│   ├── projects/           # 工作、个人开发、分享和工具项目
│   └── learning/           # 专题分析资料、持续学科学习与备考仓库
├── references/             # 可提交的阅读索引和自己的提炼
│   └── opensource-code-pro/ # 原 opensource-pro，本地阅读资料
├── local/                  # 私密资料和机器配置，本地目录
├── outputs/                # 生成文件、导出和运行产物，本地目录
└── tmp/                    # 临时内容，本地目录
```

`repos/` 内仓库和 `references/opensource-code-pro/` 不提交到 my-workspace，也不采用 submodule。克隆工作空间只会得到管理文件；需要的独立仓库按清单另行克隆。

## 开始使用

```bash
python3 scripts/setup.py
python3 scripts/repos.py list
# 根据需要克隆独立仓库，已有目录会跳过
python3 scripts/repos.py clone my-skills-market
# 或克隆所有登记的仓库：python3 scripts/repos.py clone --all
python3 scripts/repos.py status
# 进入某个仓库工作
cd repos/projects/my-skills-market
```

仓库清单见 [config/repos.json](config/repos.json)，维护方法见 [使用说明](docs/workspace-guide.md)。私有仓库可写入被忽略的 `config/repos.local.json`，格式参考 [本地清单示例](config/repos.local.example.json)。

共享技能见 [skills/README.md](skills/README.md)，全局知识见 [knowledge/README.md](knowledge/README.md)，各仓库的背景见 [仓库简介](docs/repositories.md)。这些内容与管理脚本一起随工作空间 clone / pull 同步。

新机器先克隆本仓库，再运行 `python3 scripts/setup.py` 创建本地目录；Agent 从 `AGENTS.md` 读取入口，按任务加载相关知识和技能。初始化不会自动安装技能到用户目录。

在根目录直接提出“我想学习 XXX”即可：AGENTS.md 指引 Agent 加载学习技能、定位学科并恢复进度。专题分析阅读与学习先查看 ai-coding-practice；持续学科辅导、练习与进度归入 personal-study-project，高项备考归入 my-exam-gaoxiang，系统架构设计师备考归入 my-exam-sa，具体技能入口见 skills/README.md。若工具不自动读取入口文件，请在首次任务中要求它先读 AGENTS.md。

## 同步仓库

从根目录提出“同步仓库”即可按 [workspace-git-sync](skills/workspace-git-sync/SKILL.md) 处理，也可直接运行：

```bash
python3 scripts/workspace-git-sync.py --dry-run
python3 scripts/workspace-git-sync.py
# 仅同步指定仓库
python3 scripts/workspace-git-sync.py workspace my-exam-sa
```

脚本按当前分支上游快进拉取，保留有改动或分叉的仓库并汇总；不会自动提交或推送。

## 内容放哪里

| 任务 | 默认归属 |
|---|---|
| 阅读文章、视频并收录提炼 | `repos/notes/my-daily-remarks/` |
| 阅读源码讲解、AI 分析笔记，开展专题学习或调研 | `repos/learning/ai-coding-practice/` |
| 按学科持续学习、练习、复习与追踪进度 | `repos/learning/personal-study-project/` |
| 高项概念复习、案例与论文训练 | `repos/learning/my-exam-gaoxiang/` |
| 软考系统架构设计师考试备考资料 | `repos/learning/my-exam-sa/` |
| 记录项目工作、日志和领域资料 | `repos/notes/my-obsidian-notes/` |
| 提炼长期知识卡片、建立知识连接 | `repos/notes/my-obsidian-knowledge-base/` |
| 整理公开的 AI 观察文章 | `repos/notes/my-ai-observe-notes/` |
| 制作 AI 协作编程分享、大纲、讲稿与 PPT | `repos/projects/ai-coding-share/` |
| 维护和分发共享技能、插件 | `repos/projects/my-skills-market/` |

专题调研也可以保存在 Obsidian 笔记库的独立文件夹中。上表提供默认导航；用户指定的位置和已有专题优先，按主题保持一份主要正文，通过链接关联其他仓库。

工作空间本身保存跨项目计划 `plans/`、工作概览与复盘 `journal/`、跨主题技术总结 `learning/`、阅读索引 `references/` 和成熟方法 `knowledge/`。项目已有记录和学科进度保留在原仓库，避免再建立一份重复正文或追踪器。

计划和日常记录可参考 [项目模板](templates/project.md) 与 [记录模板](templates/journal.md)。原始参考源码、下载资料放本地参考目录；具体落点和写入要求见 [仓库索引](docs/repositories.md)。

工作空间里的内容会随着后续提交进入 Git 历史。涉及个人隐私的笔记正文放私有笔记库或 `local/`；提交前查看暂存内容。

当前整理结果见 [初次整理记录](docs/initial-layout.md)。
