# 仓库简介

机器可读清单以 [config/repos.json](../config/repos.json) 为准。本页帮助理解用途，不包含独立仓库正文。

## 按任务选择仓库

| 任务或内容 | 仓库 | 本地位置 | 读取入口与写入建议 |
|---|---|---|---|
| 收录文章、视频，阅读提炼，周总结 | my-daily-remarks | repos/notes/my-daily-remarks | README.md、templates/note.md；正文放 notes/YYYY/YYYY-MM/，同步月度 _index.md；二次提炼放 summaries/ |
| 准备公开 AI 观察文章、维护笔记站 | my-ai-observe-notes | repos/notes/my-ai-observe-notes | README.md、mkdocs.yml、docs/blog/；当前文章放 docs/blog/posts/，写前参考现有文章格式；推送 main 会触发站点构建与发布 |
| AI 编程分享、演示、讲稿与幻灯片 | ai-coding-share | repos/projects/ai-coding-share | README.md、CLAUDE.md 与 output/ 目标版本大纲；想法放 my-ideas/，参考放 reference/，讲稿和幻灯片按版本维护；2026-10-10 推送确认远端已归档只读，可查询与本地修改，远端更新需另行处理归档状态 |
| 维护可分发的技能或插件 | my-skills-market | repos/projects/my-skills-market | README.md、目标插件的 SKILL.md；共享技能索引见工作空间 skills/README.md |
| 链企 AI 标书写作的复刻实现（自用，自选模型、无计费，聚焦标书写作） | my-lianqi-ai-copy | repos/projects/my-lianqi-ai-copy | README.md、research/；对标产品的调研资料放 research/，设计与工程实现后续在同仓库进行 |
| 用于个人学习的 AI 分析笔记、源码讲解、Agent 研究与调研 | ai-coding-practice | repos/learning/ai-coding-practice | README.md、编号主题目录与专题 README；按问题阅读与复习，补充分析时同步索引并记录来源和验证范围；持续学科练习另归 personal-study-project |
| 多学科持续学习、练习与复习 | personal-study-project | repos/learning/personal-study-project | README.md、学科配置与追踪器；先按 skills/README.md 加载学习技能，再接续已有学科 |
| 项目工作笔记、工作日志、领域资料与专题调研 | my-obsidian-notes | repos/notes/my-obsidian-notes | README.md、01项目Project/、02领域Area/ 与相邻笔记；待整理内容放 00-Inbox/，保留链接与附件 |
| 长期知识积累、阅读卡片、个人专题研究与跨领域连接 | my-obsidian-knowledge-base | repos/notes/my-obsidian-knowledge-base | README.md、CLAUDE.md、03-MOC/；来源放 01-Sources/，永久笔记放 02-Notes/ 并同步 MOC；遵守 wiki 自动维护约定 |
| 高项备考计划、资料消化与模考 | my-exam-gaoxiang | repos/learning/my-exam-gaoxiang | README.md、03-计算案例/、04-论文专项/、06-核心概念必背/ 的实际追踪文件；01-备考资料/ 原料只读，应试规划加载 ispm-exam-coach |
| 系统架构设计师考试备考资料 | my-exam-sa | repos/learning/my-exam-sa | README.md；当前仅有备考标题，尚无资料目录和进度记录，按实际学习需要逐步补充 |

## 留在工作空间的内容

| 内容 | 位置 | 使用建议 |
|---|---|---|
| 跨项目或尚未落地的计划 | plans/ | 有明确目标、阶段和下一步时记录，参考 templates/project.md |
| 日常完成情况与复盘 | journal/ | 按年份归档，参考 templates/journal.md |
| 跨项目技术总结 | learning/ | 专题学习分析归 ai-coding-practice，学科会话和练习归 personal-study-project，这里保存跨主题总结 |
| 阅读索引与跨项目资料提炼 | references/ | 来源正文已有专属仓库时在这里保留链接，避免重复；opensource-code-pro/ 为本地参考源码 |
| 可复用的习惯、方法与决策 | knowledge/ | 按 knowledge/README.md 组织，注明适用范围和容易变化的事实的核实日期 |
| 共享技能源与技能路由 | skills/ | 按 skills/README.md 维护；已有市场源通过引用复用 |

## 如何使用这份索引

以上用途帮助选定范围；实际路径与远端以公共清单和可选本地清单为准，具体写入方式以目标仓库当前约定为准。落点优先遵循用户指定的仓库或目录，其次沿用已有专题，最后按默认用途选择。专题调研也可放在 Obsidian 库的独立文件夹：工作相关专题倾向工作库，个人长期研究倾向知识库。无需迁移已有资料或在多个仓库重复正文；具体归属仍不明确时再补问。

登记不代表本地已克隆，工作树状态也不保存在本索引中。运行 `python3 scripts/repos.py list` 查看登记，运行 `python3 scripts/repos.py status` 查看本地状态。新增或变更归属时同步清单和本页。详细操作见 [Agent 使用指南](agent-guide.md)。

核实日期：2026-10-10。本次检查九个登记仓库的根目录、README、存在的根级协作约定与相关索引；用途结合用户对学习方式的说明修正。目录和文档检查不代表子项目、技能、OCR 工具或线上站点已运行验证。分支与改动状态按任务实时查询，不固定在索引中。

2026-10-10：新增并克隆 my-exam-sa，清单现有十个仓库。新仓库当前仅有 README 标题，尚未建立备考资料目录或学习追踪记录。

2026-10-12：新增并克隆 my-lianqi-ai-copy（清单现有十一个仓库），用于链企 AI 标书写作的复刻实现（自用）。对标产品调研资料已归入其 research/（功能架构、API 清单、登录后实测记录），设计与工程实现将在同仓库继续进行。
