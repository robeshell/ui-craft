# UI Craft

A task-driven UI design and refinement skill for coding agents. 中文编写，适用于网页与原生 App。

从用户任务确定视觉主次，用分组、对齐、重复和对比组织信息，再把品牌、文字、图标、间距和状态落实到可验证的界面。

## 适用场景

- 功能区分不清、所有模块同等强调，页面像线框原型。
- 文字与数字对齐、真实内容换行、圆角、图标和间距需要精修。
- 多页样式不一致，需要整理可维护的设计规范。
- 对已有页面做有依据的视觉和交互检查。

不预设主题、品牌色、字体或布局模板；局部修正不强制重做整个设计系统。保留现有产品与业务约束。可独立使用，better 系列仅是可选补充。

## 安装到 Codex

先将仓库克隆到本地，再将整个目录复制到 Codex 的 skills 目录。目标目录已存在时先比较内容，避免覆盖本地修改。

```bash
git clone https://github.com/robeshell/ui-craft.git
mkdir -p ~/.codex/skills
# 确认 ~/.codex/skills/ui-craft 尚不存在后执行：
cp -R ui-craft ~/.codex/skills/ui-craft
```

开始新对话后使用：

```text
使用 $ui-craft 精修当前页面。先判断主要任务和功能优先级，
保留已有品牌与业务，调整信息分组与视觉细节，并验证实际渲染。
```

其他支持 SKILL.md 的工具可按各自的技能安装方式使用本目录；未逐一验证客户端兼容性。

## 文件

- [SKILL.md](SKILL.md)：入口与核心设计流程。
- [视觉决策规则](references/visual-rules.md)：文字、色彩、布局、平台单位、图标和状态。
- [检查与交付](references/review.md)：验证范围、证据和评审表达。
- [来源与边界](references/sources.md)：CRAP、公开教程及实践的归属和取舍。
- [contrast.py](scripts/contrast.py)：只依赖 Python 3 标准库的不透明 sRGB 色对对比度计算。

```bash
python3 scripts/contrast.py '#222222' '#FFFFFF'
```

脚本结果只反映指定色对，不能证明整个页面符合无障碍标准。网页预览也不能替代原生真机验证。

## 贡献与许可

欢迎通过 Issue 提供具体页面问题、使用场景与验证结果，或提交有明确原因的改进。请勿上传私人项目资料、账号、截图中的个人信息或无权分发的素材。

仓库原创内容采用 [MIT License](LICENSE)。链接指向的书籍、教程、图片和其他第三方内容不属于此许可；本仓库不附带其素材，也不代表相关作者的官方发布。
