# my-workspace

个人工作的总入口：组织独立仓库，记录计划、学习与思考，积累能长期复用的经验。

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
│   └── learning/           # 学习练习和实验仓库
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

在根目录直接提出“我想学习 XXX”即可：AGENTS.md 指引 Agent 加载学习技能、定位学科并恢复进度。通用技术学习归入 personal-study-project，高项备考归入 my-exam-gaoxiang，具体技能入口见 skills/README.md。若工具不自动读取入口文件，请在首次任务中要求它先读 AGENTS.md。

## 内容放哪里

- 项目源码、项目文档：对应的 `repos/projects/<name>/`。
- 两个 Obsidian 库：`repos/notes/my-obsidian-notes/` 和 `repos/notes/my-obsidian-knowledge-base/`，各自保持原仓库历史和 `.obsidian/` 配置。
- 日常工作与复盘：`journal/YYYY/`，使用 [记录模板](templates/journal.md)。
- 业余项目计划：`plans/<project>.md`，使用 [项目模板](templates/project.md)；开始编码后新建独立项目仓库。
- 技术学习：总结放 `learning/<topic>/`，较大的代码练习放独立学习仓库。
- 资料阅读：链接和自己的提炼放 `references/`；完整源码、下载资料留在本地参考目录。

工作空间里的内容会随着后续提交进入 Git 历史。涉及个人隐私的笔记正文放私有笔记库或 `local/`；提交前查看暂存内容。

当前整理结果见 [初次整理记录](docs/initial-layout.md)。
