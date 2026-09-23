# 来源与边界

UI Craft 是结合 CRAP 原则、公开教程和实际 UI 迭代经验整理的独立工作方法。它不是任何教程作者、平台或组织发布的官方 skill。仓库不复制教程图片、完整讲义或网站素材，原图、原文及其权利归相应作者。查看原教学示例请访问下列原站。

来源整理日期：2026-09-22。链接指向的外部内容可能更新，涉及平台 API、发行要求或标准状态时以当前官方文档为准。

## 方法的三个来源

**CRAP 原则。** 亲密性、对齐、重复、对比，出自 Robin Williams《写给大家看的设计书》（The Non-Designer's Design Book）。本 skill 采用这四条组织信息，第 2 步的处理顺序是本 skill 自己的安排，不声称逐字引用原书。

**公开教程。** 前身以 [JumpDesign UI 教程](https://tutorial.jumpdesign.tw/ui_tutorial.html)为起点，从中提炼了单位与尺度、色彩对比、图标设计、跨平台规范、网页组成与结构等主题的判断方法。取舍见下表。

**实际迭代经验。** 以下判断来自多个项目反复验证，是可迁移的方法，不是固定模板：

- 功能重要性决定面积，功能数量不决定。
- 只靠描边分区会保留原型感。
- 并列布局必须容纳真实内容长度。
- 可见间距不等于声明的尺寸。
- 系统栏、Safe Area、键盘约束必须在实现里落地，不能只画在稿子上。

## 教程到方法的映射

| 教程 | 提炼内容 | 取舍 |
| --- | --- | --- |
| [UI 基本设计规范](https://tutorial.jumpdesign.tw/handouts/ui/ui-concept.html) | 单位、尺度、间距、触控区、圆角与资源交付 | 不沿用有歧义的像素换算示例；原生单位按官方资料核对 |
| [色彩对比度](https://tutorial.jumpdesign.tw/handouts/ui/color-contrast.html) | 前景与背景组合、文字和非文字识别 | 以 W3C 定义区分阈值及例外，校正 APCA 的标准状态说法 |
| [UI 项目规范企划书](https://tutorial.jumpdesign.tw/handouts/ui/ui-project/) | 目标、使用者任务、信息架构、设计规范、组件与展示的关系 | 调研方法按任务选用，不制造问卷、人物画像或竞品数据 |
| [图标设计](https://tutorial.jumpdesign.tw/handouts/ui/icon-design/) | 语义识别、风格、视觉面积、重心和网格 | 图标风格示例用于比较，不混用全部风格 |
| [iOS / Android 设计规范](https://tutorial.jumpdesign.tw/handouts/ui/iOS-Android/) | 逻辑尺寸与导出倍率、文字层级、导航关系 | 历史机型、固定栏高和字号例值不是现行跨平台规范 |
| [网页型态解析](https://tutorial.jumpdesign.tw/handouts/ui/web-type/) | 产品类型与信息组织、用户目标的关系 | 不将建站平台清单写成当前技术推荐 |
| [网页组成与设计规范](https://tutorial.jumpdesign.tw/handouts/ui/web-composition/) | 字体完整属性、亲疏关系、组件及状态、响应式 | 网页间距与 hover 不自动套到手机原生应用 |
| [网页结构与排版](https://tutorial.jumpdesign.tw/handouts/ui/web-structure/) | 内容整理、区块、调性、动线、对比与强调 | 展示型页面的装饰不作为任务型界面的固定套路 |
| [网站制作流程](https://tutorial.jumpdesign.tw/handouts/ui/web-production/) | 从内容和架构到规范、样板、页面与验证 | 主机、域名、FTP、推广及报价不属于此 skill |
| [Figma](https://tutorial.jumpdesign.tw/handouts/ui/Figma/) | 文本属性、组件、协作与交互原型的用途 | 不复刻旧版界面、快捷键或插件清单，不要求安装工具 |
| [Adobe XD](https://tutorial.jumpdesign.tw/handouts/ui/Adobe-XD/) | 样式与组件管理、画板和预览尺度 | 不强制采用该软件 |
| [成果发表技巧](https://tutorial.jumpdesign.tw/handouts/ui/work-published/) | 清晰展示、来源、设备与输出检查 | 求职履历和演讲技巧不纳入 UI 实施规则 |

## 校正和补充依据

- [W3C：文字对比度](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)：普通文字、符合定义的大号文字及例外分别判断。
- [W3C：非文字对比度](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)：用于识别必要控件、状态和图形，不要求所有纯装饰边界达到同一阈值。
- [W3C：相对亮度定义](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)：`scripts/contrast.py` 采用此处的 sRGB 线性化与相对亮度计算。
- [WCAG 3.0](https://www.w3.org/TR/wcag-3.0/)：整理时仍是 Working Draft。APCA 未正式取代 WCAG 2.x。
- [Android Compose：无障碍默认行为](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)：触控目标与可见图形尺寸分开考虑。
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)：文本样式、Dynamic Type、Safe Area、44pt 触控目标。
- [Material Design 3](https://m3.material.io/)：Type scale、48dp 触控目标。
- [华为 DevEco 推荐规则](https://developer.huawei.com/consumer/cn/doc/doccenter-deveco-studio/ide-coderlinter-recommended-rules)：`font-size-unit` 与 `size-unit` 分别对应 fp 和 vp。

## 临时基线的性质

`references/visual-rules.md` 里标注为"临时基线"的数值，是从上述平台规范和常见项目实践里取的中间值，用于项目没有规范时起步。它们不是任何教程或平台的强制要求，也不是本 skill 推荐的唯一风格。项目一旦有自己的 tokens 或规范，临时基线就应被替换。

## 什么不通用化

具体项目的品牌色、画布尺寸、图表切换位置、面板半径和导航样式属于项目规范，不归因于 CRAP 或教程，也不要求其他产品照搬。本 skill 只保留能解释多个场景的判断方法。
