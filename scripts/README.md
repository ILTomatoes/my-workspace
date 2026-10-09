# 工作空间工具

仅依赖 Python 3.9+ 标准库与 Git，从任意工作目录调用均可。

- `python3 scripts/setup.py`：创建本地目录，可重复运行，不改动现有仓库。
- `python3 scripts/repos.py list`：列出仓库和路径。
- `python3 scripts/repos.py status`：查看存在性、分支和改动。
- `python3 scripts/repos.py clone <name> ...`：克隆指定仓库。
- `python3 scripts/repos.py clone --all`：克隆清单中所有尚无本地路径的仓库。

清单自动合并 config/repos.json 与可选的 config/repos.local.json。已有路径始终跳过；不会自动 pull、reset、提交或推送。克隆失败会返回非零状态，可能留下 Git 的部分目录，需要查看原因后自行处理。
