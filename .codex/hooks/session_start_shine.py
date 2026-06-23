"""Print the SS14-ART-CORE instruction entry points for Codex sessions."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

print("SS14-ART-CORE: load .agents/skills/ss14-art-core/SKILL.md first.")
print("Hard rules: no RobustToolbox edits, new code under _Art, mark non-_Art edits with Art-Start/Art-End.")
print(f"Rules: {ROOT / '.agents' / 'rules'}")
