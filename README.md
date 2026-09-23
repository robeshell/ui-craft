# UI Craft

[![npx skills add robeshell/ui-craft](https://img.shields.io/badge/npx-skills%20add%20robeshell%2Fui--craft-CB3837?logo=npm&logoColor=white)](#usage)

English · [中文](README.zh-CN.md)

A UI design skill for coding agents such as Claude Code and Codex. It gives the agent a product designer's judgment for functional interfaces: admin panels, dashboards, tools, and app screens. The skill itself is written in Chinese.

Instead of making pages "prettier", it makes the agent answer one question before touching any style: **what does the user come to this page to do?** Visual weight, grouping, color, and detail all follow from that answer.

## What it does

- **Task-driven hierarchy.** Derives what should dominate a page from the user's task, not from how many modules there are. Eight modules do not become eight equal cards.
- **Restraint.** Two hard rules override everything else. A page that already works gets a "no change needed" reply instead of a diff. A project's own spec (`DESIGN.md`, `AGENTS.md`, `CLAUDE.md`, tokens, component library) outranks the skill's rules unless the user explicitly says otherwise.
- **Tune-up mode.** A vague "optimize this page" is handled by diffing the page against the standard layout for its type, ranking the gaps by impact, and fixing only the top few.
- **Standard layouts.** Thirteen common page types (workbench, query list, detail, form, analytics, settings, processing queue, empty state, and five mobile patterns) with their mature structure and the mistakes AI-generated versions usually make.
- **Color that carries meaning.** A surface layering model, a color budget (one accent, neutrals, status colors), and a checklist of AI-look patterns: purple gradients, rainbow KPI cards, icon tiles, glow shadows, gray chips on every row.
- **Honest verification.** Contrast is computed at full precision, not eyeballed. Delivery separates "rule defined", "code written", "rendered", "interaction verified", and "accepted by user".
- **Two scripts.** `contrast.py` for WCAG contrast with alpha compositing; `surfaces.py` to generate brand-tinted neutral surfaces for light and dark mode.

It does not do marketing or landing pages, does not pick a theme color from scratch, and does not decide feature scope. It governs the interface; features come from the user's request.

## Usage

Install for Claude Code and Codex in one command:

```bash
npx skills add robeshell/ui-craft -g -a claude-code -a codex -y
```

Update later with `npx skills update`. Manual install: clone the repo and copy the folder to `~/.claude/skills/ui-craft` or `~/.codex/skills/ui-craft`.

Then invoke it as `/ui-craft` in Claude Code or `$ui-craft` in Codex, or just describe the problem. Requests that mention layout, hierarchy, color, spacing, "looks like a prototype", or "looks AI-generated" trigger it automatically.

```text
/ui-craft 帮我优化一下这个页面
/ui-craft 这个页面有点 AI 味，颜色太花
/ui-craft 看看 SettingsScreen.kt 有什么视觉问题
/ui-craft 用 Vue 写一个订单列表页
```

The agent first decides which mode the request is in (local fix, page design, tune-up, spec, review, or no change) and does only that much work.

## Methodology

**Step 0. Decide the mode and read the constraints.** Existing brand, spec files, real content, target platform. Then the two hard rules: do not optimize for its own sake, and the project's spec wins over the skill.

**Step 1. Derive visual weight from the task.** Write one sentence: "On this page the user needs to ____." Rank content as P0 (watched continuously), P1 (needed to decide), P2 (the main action), P3 (everything else). Map the ranks to area, position, contrast, and whitespace. For common page types, take the standard structure from `references/patterns.md`.

**Step 2. Organize space by information relationships.** Proximity, alignment, repetition, contrast, in that order. Group first, choose containers second. Continuous, same-shaped items become list rows; independent objects become cards. One kind of emphasis per focal point.

**Step 3. Build product expression.** Pick two or three visual traits that run through the page and say what each one serves. Decoration follows rules: shadows for floating layers, gradients only where the brand demands, color only where it means something.

**Step 4. Apply the detail rules.** Text roles with size, weight, line height, color, and overflow behavior. Contrast against the actual background. Icons, touch targets, radii, spacing roles, component states. Provisional baselines exist for projects with no spec and are labeled as such.

**Step 5. Verify on the real thing and deliver.** Check at the target viewport with real content and states. Report what was rendered, what was not, and what remains uncovered.

The full method, decision tables, and worked example live in [SKILL.md](SKILL.md) and `references/`.

## License

MIT for the repository's own content. Linked books and platform documents belong to their authors.
