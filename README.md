# UI Craft

[![npx skills add robeshell/ui-craft](https://img.shields.io/badge/npx-skills%20add%20robeshell%2Fui--craft-CB3837?logo=npm&logoColor=white)](#安装)

给 coding agent 用的 UI 设计与精修 skill。适用于网页和 iOS / Android / HarmonyOS 原生应用，中文编写。

它让 agent 在动手改样式之前先回答一个问题："用户在这个页面要完成什么？"然后把视觉权重、信息分组、品牌表达和细节规则依次落到可验证的实现上。核心是判定规则加一份完整示例，而不是一套固定主题。

## 什么时候用

- 页面所有模块等大、同款，看着像线框原型，找不到重点。
- 文字与数字对不齐、真实内容换行、圆角和间距不一致，需要精修。
- 多个页面样式不统一，需要整理一份可维护的设计规范。
- 对已有页面做有依据的视觉和交互评审，而不是"感觉不够高级"。
- 从零生成一个带 UI 的页面或组件，希望它一开始就有主次和层级。

不预设主题、品牌色、字体或布局模板。项目已有的品牌、组件库和规范优先；没有规范时提供一份标注为"临时基线"的起始值表。局部修正不会被扩大成整套重构。

## 安装

**推荐：用 npx 一条命令安装**

```bash
npx skills add robeshell/ui-craft -g -a claude-code -a codex -y
```

这条命令用的是 npm 上的 [skills](https://github.com/vercel-labs/skills) 工具，它直接从本仓库的 main 分支拉取。

- `-g` 装到用户级目录，所有项目都能用。去掉它就只装进当前项目。
- `-a` 指定装给哪个工具，只用 Claude Code 就只写 `-a claude-code`。
- `-y` 跳过确认。不加的话会逐步询问装给哪些工具、装到哪里。

装好后，文件在 `~/.agents/skills/ui-craft`，Codex 直接读这里。`~/.claude/skills/ui-craft` 是指向它的链接，供 Claude Code 使用。两边共用一份文件，以后更新只需要：

```bash
npx skills update
```

之前用 `cp` 手动装过的话，先删掉旧的 `~/.claude/skills/ui-craft` 和 `~/.codex/skills/ui-craft`，避免重复。

**手动安装**

不想用 npx 时，克隆仓库后复制到对应目录。

```bash
git clone https://github.com/robeshell/ui-craft.git

# Claude Code
mkdir -p ~/.claude/skills && cp -R ui-craft ~/.claude/skills/ui-craft

# Codex
mkdir -p ~/.codex/skills && cp -R ui-craft ~/.codex/skills/ui-craft
```

只想在某个项目里用，就复制到该项目的 `.claude/skills/ui-craft`。其他支持 `SKILL.md` 的工具按各自的方式放置本目录即可。目标目录已存在时先比较内容，避免覆盖本地修改。

## 使用

安装后，涉及界面、布局、排版、配色、设计规范的请求会自动触发。也可以直接点名：

```text
用 ui-craft 重排这个工作台首页。客服在这页主要是接工单，
保留品牌蓝和现有功能，其他都可以动。
```

```text
用 ui-craft 看看 src/pages/Settings.vue 有什么视觉问题，按影响排序。
```

```text
用 ui-craft 把这三个页面的文字、颜色和间距整理成一份 DESIGN.md。
```

agent 会先判断任务是局部修正、页面重排、规范整理还是评审，再决定走多少步骤。交付里会分开写明"规则已定义、代码已实现、渲染已检查、交互已验证、用户已接受"，不会把没跑过的东西说成已验证。

## 文件

| 文件 | 内容 | 何时读 |
| --- | --- | --- |
| [SKILL.md](SKILL.md) | 入口：任务模式判断、五步流程、交付格式、精简示例 | 每次触发 |
| [references/example.md](references/example.md) | 一个客服工单页从等大卡片到任务驱动的完整推演，含规范表和实查记录 | 遇到主次不清的页面 |
| [references/visual-rules.md](references/visual-rules.md) | 文字、单位、色彩、间距、圆角、图标、状态、动效的判定规则和临时基线 | 处理具体细节时 |
| [references/color-layers.md](references/color-layers.md) | 表面分层、颜色预算、大色块、图标底块、渐变的判定规则，以及 AI 味特征清单 | 页面颜色太花、有 AI 味、深色模式分不清层次时 |
| [references/review.md](references/review.md) | 检查范围、检查表、证据边界、评审表达、交付记录模板 | 验收和交付时 |
| [references/sources.md](references/sources.md) | CRAP、教程和平台文档的归属与取舍 | 需要追溯来源时 |
| [scripts/contrast.py](scripts/contrast.py) | sRGB 色对对比度计算，支持透明色合成 | 校验文字颜色时 |
| [scripts/surfaces.py](scripts/surfaces.py) | 从品牌色生成带色调的中性灰阶，浅色和深色各一套，附对比度 | 项目没有 tokens、需要一套表面色时 |
| [evals/evals.json](evals/evals.json) | 九个测试 prompt 和评判标准，输入文件在 `evals/files/`，用于比较装与不装 skill 的输出差异 | 修改 skill 后 |

```bash
python3 scripts/contrast.py '#767676' '#FFFFFF'
python3 scripts/contrast.py 'rgba(0,0,0,0.6)' '#F5F5F5' --over '#FFFFFF'
```

脚本只回答一个色对的比值，不能证明整个页面符合无障碍标准。

## 贡献与许可

欢迎通过 Issue 提供具体的页面问题、使用场景和验证结果，或提交有明确原因的改进。修改 skill 后建议用 `evals/evals.json` 里的 prompt 跑一遍，确认改动真的改变了输出。请勿上传私人项目资料、账号、截图中的个人信息或无权分发的素材。

仓库原创内容采用 [MIT License](LICENSE)。链接指向的书籍、教程和第三方内容不属于此许可；本仓库不附带其素材，也不代表相关作者的官方发布。
