# SS14 Code Placement

## Assembly Boundaries

> **Config:** Actual fork values (`FORK_DIR`, `EDIT_MARKER`, `FORK_NAME`) are defined in `.agents/fork-config.md`.

- `Content.Shared`: data and logic both client and server may run; predicted gameplay belongs here when possible.
- `Content.Server`: authoritative-only logic, persistence, admin-only server work, atmos/power-only flows that cannot be predicted.
- `Content.Client`: rendering, XAML/BUI client windows, visualizers, overlays, input UI, client-only presentation.
- `Resources`: prototypes, maps, textures, audio, localization, guidebook data.
- `Content.Tests` and `Content.IntegrationTests`: focused validation.
- `RobustToolbox`: read-only for {FORK_NAME} agents.

## SS14-ART-CORE Placement

New {FORK_NAME} code must use `{FORK_DIR}` path segments:

- `Content.Shared/{FORK_DIR}/<Subsystem>/...`
- `Content.Server/{FORK_DIR}/<Subsystem>/...`
- `Content.Client/{FORK_DIR}/<Subsystem>/...`
- `Resources/Prototypes/{FORK_DIR}/<Subsystem>/...`
- `Resources/Locale/en-US/{FORK_DIR}/<Subsystem>/...`

Preserve SS14 folder semantics under `{FORK_DIR}`: `Components`, `EntitySystems`, `UI`, `Visualizers`, `Prototypes`, etc.

## Upstream Files

Only touch non-`{FORK_DIR}` files when integration requires it. Keep the diff narrow and apply `{EDIT_MARKER}-Edit` markers around the exact changed lines.
