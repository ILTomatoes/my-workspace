# my-workspace

个人工作的总入口：组织独立仓库，记录计划、学习与思考，积累能长期复用的经验。

借鉴 aip-workspace 的「工作空间 + 独立仓库 + 仓库清单」方式，先保持轻量；具体源码、完整笔记和项目历史留在各自仓库。

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

## 内容放哪里

- 项目源码、项目文档：对应的 `repos/projects/<name>/`。
- 两个 Obsidian 库：`repos/notes/my-obsidian-notes/` 和 `repos/notes/my-obsidian-knowledge-base/`，各自保持原仓库历史和 `.obsidian/` 配置。
- 日常工作与复盘：`journal/YYYY/`，使用 [记录模板](templates/journal.md)。
- 业余项目计划：`plans/<project>.md`，使用 [项目模板](templates/project.md)；开始编码后新建独立项目仓库。
- 技术学习：总结放 `learning/<topic>/`，较大的代码练习放独立学习仓库。
- 资料阅读：链接和自己的提炼放 `references/`；完整源码、下载资料留在本地参考目录。

工作空间里的内容会随着后续提交进入 Git 历史。涉及个人隐私的笔记正文放私有笔记库或 `local/`；提交前查看暂存内容。

当前整理结果见 [初次整理记录](docs/initial-layout.md)。
