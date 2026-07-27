# Fork Configuration

Single source of truth for fork-specific values.
Change these when forking this repository.

| Key | Value | Description |
|-----|-------|-------------|
| `FORK_DIR` | `_Trauma` | Directory for fork-only code under `Content.Shared/`, `Content.Server/`, `Content.Client/`, `Resources/Prototypes/`, `Resources/Locale/en-US/`, `Resources/Textures/`, `Resources/Audio/` |
| `EDIT_MARKER` | `Trauma` | Prefix for edit markers: `{EDIT_MARKER}-Edit`, `{EDIT_MARKER}-Start`, `{EDIT_MARKER}-End` |
| `FORK_NAME` | `Trauma Station` | Human-readable fork name used in instructions and comments |

To fork: change the values above. All `.agents/` instructions use these values via `{FORK_DIR}`, `{EDIT_MARKER}`, `{FORK_NAME}` template variables — no other files need editing.
