# GitHub Copilot Instructions

This repo uses `.agents` as the canonical instruction layer.

Before suggesting code, follow:

- `.agents/rules/ss14-art-hard-guardrails.md`
- `.agents/rules/ss14-art-upstream-edit-markers.md`
- `.agents/rules/ss14-skill-preflight-and-refresh.md`

Do not suggest edits to `RobustToolbox/**`. New SS14-ART-CORE code belongs in `_Art`. Any non-`_Art` edit must be surrounded by Art-Edit/Art-Start/Art-End markers. Prefer SS14 ECS, prediction, localization, typed prototypes, and .NET 10-current APIs.
