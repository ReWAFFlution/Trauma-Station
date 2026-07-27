# SS14 Assets And Attribution

Use this rule for textures, audio, RSI metadata, icons, station images, and imported content.

## Required

- Preserve source, author, license, and commit/source URL where known.
- Keep RSI `meta.json` readable and ordered.
- Do not import assets with incompatible commercial/copyleft terms without maintainer approval.
- Do not mix asset ports with unrelated code cleanup.

## SS14-ART-CORE Placement

> **Config:** Actual fork directory (`FORK_DIR`) is defined in `.agents/fork-config.md`.

- Textures: `Resources/Textures/{FORK_DIR}`.
- Audio: `Resources/Audio/{FORK_DIR}`.
- Prototype references to new assets should live under `{FORK_DIR}` unless integrating into upstream content.
