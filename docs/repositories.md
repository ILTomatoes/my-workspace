# 仓库简介

机器可读清单以 [config/repos.json](../config/repos.json) 为准。本页帮助理解用途，不包含独立仓库正文。

## 按任务选择仓库

| 任务或内容 | 仓库 | 本地位置 | 读取入口与写入建议 |
|---|---|---|---|
| 收录文章、视频，阅读提炼，周总结 | my-daily-remarks | repos/notes/my-daily-remarks | README.md、templates/note.md；正文放 notes/YYYY/YYYY-MM/，同步月度 _index.md；二次提炼放 summaries/ |
| 准备公开 AI 观察文章、维护笔记站 | my-ai-observe-notes | repos/notes/my-ai-observe-notes | README.md、mkdocs.yml、docs/blog/；当前文章放 docs/blog/posts/，写前参考现有文章格式；推送 main 会触发站点构建与发布 |
| AI 编程分享、演示、讲稿与幻灯片 | ai-coding-share | repos/projects/ai-coding-share | README.md 与对应版本目录；修改目标版本的源材料，遵循仓库自身生成流程 |
| 维护可分发的技能或插件 | my-skills-market | repos/projects/my-skills-market | README.md、目标插件的 SKILL.md；共享技能索引见工作空间 skills/README.md |
| AI 编程实践、Agent 架构研究与实验 | ai-coding-practice | repos/learning/ai-coding-practice | README.md、已有主题和实验目录；项目实验记录留在本仓库 |
| 持续技术学习、练习与复习 | personal-study-project | repos/learning/personal-study-project | README.md、学科配置与追踪器；先按 skills/README.md 加载学习技能，再接续已有学科 |
| 完整私人笔记 | my-obsidian-notes | repos/notes/my-obsidian-notes | 仓库约定、主题索引与相邻笔记；保留已有链接、附件和 Obsidian 结构 |
| 私人知识库 | my-obsidian-knowledge-base | repos/notes/my-obsidian-knowledge-base | 仓库约定、主题索引与相邻笔记；与上一个库无法明确区分时询问目标库 |
| 高项备考计划、资料消化与模考 | my-exam-gaoxiang | repos/learning/my-exam-gaoxiang | README.md 与已有进度；应试规划按 skills/README.md 加载 ispm-exam-coach |

## 留在工作空间的内容

| 内容 | 位置 | 使用建议 |
|---|---|---|
| 跨项目或尚未落地的计划 | plans/ | 有明确目标、阶段和下一步时记录，参考 templates/project.md |
| 日常完成情况与复盘 | journal/ | 按年份归档，参考 templates/journal.md |
| 跨项目技术总结 | learning/ | 持续学科学习仍归学习仓库，这里只保存跨项目总结 |
| 阅读索引与跨项目资料提炼 | references/ | 来源正文已有专属仓库时在这里保留链接，避免重复；opensource-code-pro/ 为本地参考源码 |
| 可复用的习惯、方法与决策 | knowledge/ | 按 knowledge/README.md 组织，注明适用范围和容易变化的事实的核实日期 |
| 共享技能源与技能路由 | skills/ | 按 skills/README.md 维护；已有市场源通过引用复用 |

## 如何使用这份索引

以上用途帮助选定范围；实际路径与远端以公共清单和可选本地清单为准，具体写入方式以目标仓库当前约定为准。未指定仓库时按任务选择最明确的落点；多个私人笔记库或项目都合理时再补问。

登记不代表本地已克隆，工作树状态也不保存在本索引中。运行 `python3 scripts/repos.py list` 查看登记，运行 `python3 scripts/repos.py status` 查看本地状态。新增或变更归属时同步清单和本页。详细操作见 [Agent 使用指南](agent-guide.md)。

2026-10-10：根据当前清单及两个收录/发布仓库的 README、目录和发布工作流补充任务路由；其余仓库用途沿用现有简介，未逐项验证内部工作流。索引不表示站点已经成功部署。
