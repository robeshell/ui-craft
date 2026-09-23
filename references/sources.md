# 来源与提炼边界

UI Craft 是结合 CRAP 原则、公开教程、产品界面观察和实际 UI 迭代形成的独立工作方法。前身 jumpdesign-ui 以田甜甜／JumpDesign 的公开教程为起点；现已扩展为跨项目方法，不是作者发布或授权的官方 skill。不复制教程图片、完整讲义或网站样例素材；原图、原文及其权利归相应作者／权利人。查看原教学示例请访问下列原站。

来源整理日期：2026-09-22。[教程目录](https://tutorial.jumpdesign.tw/ui_tutorial.html)。以下记录方法来源与取舍，不意味着历史教学内容已通过当前平台验证。

## 综合方法的来源与归属

- **CRAP**：依据用户提供的《写给大家看的设计书》核心原则总结，采用亲密性、对齐、重复、对比组织信息；不声称重新通读或逐字引用原书。
- **产品截图观察**：用户提供的网盘、客服、阅读、音频及个人中心画面，帮助归纳“内容关系决定分组，表面与空间共同分区，图形与字体共同形成质感”。截图只支持可见状态判断，不证明原应用的交互实现。
- **实际迭代经验**：功能重要性决定面积；过度描边保留原型感；并列布局须容纳真实内容；可见间距不同于声明尺寸；系统栏约束必须落地。它们是可迁移判断方法，不是固定布局模板。
- **better 系列**：better-layout、better-typography、better-ui 作为可选细节补充；本方法不复制其全文，不以这些 skill 的存在为前提。已研究来源为 [jakubkrehel/skills](https://github.com/jakubkrehel/skills/tree/267330e1adfc66a718fb65fa6918c1f06d0a689e/skills)。
- **项目决定不通用化**：具体品牌蓝、手机画布、图表切换位置、面板半径和导航样式留在项目规范，不归因于 CRAP 或教程，也不要求其他产品照搬。

## 前身教程研究记录

下表保留前身研究范围与取舍，不表示本次重构重新浏览了全部原站。

## 教程到方法的映射

| 教程 | 提炼内容 | 取舍 |
| --- | --- | --- |
| [UI 基本设计规范](https://tutorial.jumpdesign.tw/handouts/ui/ui-concept.html) | 单位、尺度、间距、触控区、圆角与资源交付 | 不沿用有歧义的像素换算示例；原生单位按官方资料核对 |
| [色彩对比度](https://tutorial.jumpdesign.tw/handouts/ui/color-contrast.html) | 前景／背景组合、文字和非文字识别 | 以 W3C 区分阈值及例外，校正 APCA 的标准状态说法 |
| [UI 项目规范企划书](https://tutorial.jumpdesign.tw/handouts/ui/ui-project/) · 25 页 | 目标、使用者任务、信息架构、设计规范、组件与展示的关系 | 调研方法按任务选用，不制造问卷、人物画像或竞品数据 |
| [图标设计](https://tutorial.jumpdesign.tw/handouts/ui/icon-design/) · 28 页 | 语义识别、风格、视觉面积、重心和网格 | 图标风格示例用于比较，不混用全部风格 |
| [iOS／Android 设计规范](https://tutorial.jumpdesign.tw/handouts/ui/iOS-Android/) · 20 页 | 逻辑尺寸与导出倍率、文字层级、导航关系 | 历史机型、固定栏高和字号例值不是现行跨平台规范 |
| [网页型态解析](https://tutorial.jumpdesign.tw/handouts/ui/web-type/) · 25 页 | 产品类型与信息组织、用户目标的关系 | 不将建站平台清单写成当前技术推荐 |
| [网页组成与设计规范](https://tutorial.jumpdesign.tw/handouts/ui/web-composition/) · 32 页 | 字体完整属性、亲疏关系、组件及状态、响应式 | 网页间距与 hover 不自动套到手机原生应用 |
| [网页结构与排版](https://tutorial.jumpdesign.tw/handouts/ui/web-structure/) · 37 页 | 内容整理、区块、调性、动线、对比与强调 | 展示型页面的装饰不作为任务型界面的固定套路 |
| [网站制作流程](https://tutorial.jumpdesign.tw/handouts/ui/web-production/) · 21 页 | 从内容和架构到规范、样板、页面与验证 | 主机、域名、FTP、推广及报价不属于此 skill |
| [Figma](https://tutorial.jumpdesign.tw/handouts/ui/Figma/) · 25 页 | 文本属性、组件、协作与交互原型的用途 | 不复刻旧版界面、快捷键或插件清单，不要求购买／安装工具 |
| [Adobe XD](https://tutorial.jumpdesign.tw/handouts/ui/Adobe-XD/) · 9 页 | 样式与组件管理、画板和预览尺度 | 不强制采用该软件，不把历史操作说明作为当前指南 |
| [成果发表技巧](https://tutorial.jumpdesign.tw/handouts/ui/work-published/) · 8 页 | 清晰展示、来源、设备与输出检查 | 求职履历和演讲技巧不纳入 UI 实施规则 |

## 校正和补充依据

- [W3C：文字对比度](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)：普通文字、符合定义的大号文字及例外分别判断；图片中的文字不能简单按非文字阈值处理。
- [W3C：非文字对比度](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)：用于识别必要控件、状态和图形，不要求所有纯装饰边界都达到同一阈值。
- [W3C：相对亮度定义](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)：辅助脚本采用 sRGB 线性化与相对亮度计算。
- [WCAG 3.0](https://www.w3.org/TR/wcag-3.0/)：研究时仍是 Working Draft；正式应用标准前需核对最新状态，不能认为 APCA 已全面取代 WCAG 2.x。
- [Android Compose：无障碍默认行为](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)：触控目标与可见图形尺寸分开考虑。
- [华为推荐规则](https://developer.huawei.com/consumer/cn/doc/doccenter-deveco-studio/ide-coderlinter-recommended-rules)：`font-size-unit` 与 `size-unit` 分别对应 fp 和 vp 的使用建议。

skill 中的工作流、检查表、场景化起始值、业务边界和证据分级是此次编写的应用方法，不宣称为教程作者逐字规则或平台官方规范。处理平台 API、发行要求、标准状态或工具操作时重新查证当前官方文档；一般排版任务无需每次重读整个网站。
