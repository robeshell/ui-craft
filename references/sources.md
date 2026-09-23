# 来源与边界

UI Craft 是结合 CRAP 原则、平台官方规范和实际 UI 迭代经验整理的独立工作方法。它不是任何作者、平台或组织发布的官方 skill。仓库不附带任何第三方素材，引用的书籍和文档的权利归各自的作者和权利人。

来源整理日期：2026-09-22。链接指向的外部内容可能更新，涉及平台 API、发行要求或标准状态时以当前官方文档为准。

## 方法的三个来源

**CRAP 原则。** 亲密性、对齐、重复、对比，出自 Robin Williams《写给大家看的设计书》（The Non-Designer's Design Book）。本 skill 采用这四条组织信息，第 2 步的处理顺序是本 skill 自己的安排，不声称逐字引用原书。

**平台官方规范。** 单位、文本样式、触控目标、对比度阈值等数值以下面列出的 W3C、Apple、Google、华为文档为准。skill 里的判定规则是对这些文档的应用，不替代它们。

**实际迭代经验。** 以下判断来自多个项目反复验证，是可迁移的方法，不是固定模板：

- 功能重要性决定面积，功能数量不决定。
- 只靠描边分区会保留原型感。
- 并列布局必须容纳真实内容长度。
- 可见间距不等于声明的尺寸。
- 系统栏、Safe Area、键盘约束必须在实现里落地，不能只画在稿子上。
- 用颜色冒充重要性是 AI 生成页面的共同根因。
- 页面已经满足任务时，不改也是一种交付。

## 校正和补充依据

- [W3C：文字对比度](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)：普通文字、符合定义的大号文字及例外分别判断。
- [W3C：非文字对比度](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)：用于识别必要控件、状态和图形，不要求所有纯装饰边界达到同一阈值。
- [W3C：相对亮度定义](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)：`scripts/contrast.py` 和 `scripts/surfaces.py` 采用此处的 sRGB 线性化与相对亮度计算。
- [WCAG 3.0](https://www.w3.org/TR/wcag-3.0/)：整理时仍是 Working Draft。APCA 未正式取代 WCAG 2.x。
- [Android Compose：无障碍默认行为](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)：触控目标与可见图形尺寸分开考虑。
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)：文本样式、Dynamic Type、Safe Area、44pt 触控目标。
- [Material Design 3](https://m3.material.io/)：Type scale、48dp 触控目标。
- [华为 DevEco 推荐规则](https://developer.huawei.com/consumer/cn/doc/doccenter-deveco-studio/ide-coderlinter-recommended-rules)：`font-size-unit` 与 `size-unit` 分别对应 fp 和 vp。
- OKLab / OKLCH 色彩空间：`scripts/surfaces.py` 用它生成带色调的中性灰阶，转换公式来自 Björn Ottosson 的公开定义。

## 临时基线的性质

`references/visual-rules.md` 和 `references/color-layers.md` 里标注为"临时基线"的数值，是从上述平台规范和常见项目实践里取的中间值，用于项目没有规范时起步。它们不是任何平台的强制要求，也不是本 skill 推荐的唯一风格。项目一旦有自己的 tokens 或规范，临时基线就应被替换。

## 什么不通用化

具体项目的品牌色、画布尺寸、图表切换位置、面板半径和导航样式属于项目规范，不归因于 CRAP 或平台文档，也不要求其他产品照搬。本 skill 只保留能解释多个场景的判断方法。
