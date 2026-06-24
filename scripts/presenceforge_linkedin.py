#!/usr/bin/env python3
"""PresenceForge — LinkedIn headline + About draft via Gemini (human gate before publish)."""

import os
import sys
from datetime import datetime
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parents[1]
FORGE_ROOT = Path.home() / "AI_Mastery_Project"
sys.path.insert(0, str(FORGE_ROOT))

from agents.gemini_bridge import GeminiBridge, SOVEREIGN_SYSTEM_PROMPT  # noqa: E402

OUTPUT_DIR = V2_ROOT / "docs" / "research" / "presenceforge_outputs"
GROK_PATH = V2_ROOT / "00_Overview_and_Tracking" / "GROK.md"
PROMPT1_PATH = V2_ROOT / "docs" / "research" / "phase1_prompt1_market_presenceforge.md"


def load_context() -> str:
    parts = []
    for path in (GROK_PATH, PROMPT1_PATH):
        if path.exists():
            parts.append(f"## {path.name}\n{path.read_text(encoding='utf-8')[:4000]}")
    return "\n\n".join(parts)


def main():
    context = load_context()
    prompt = f"""Create a LinkedIn profile refresh for Johann Hendrik Reyneke (FalconUnhinged).

Context documents:
{context}

Deliver exactly these sections in Markdown:

## Headline
(One line, max 220 chars, neutral corporate tone per GROK.md §1.1)

## About
(3 short paragraphs + bullet list of current projects. English primary. 
Remove "boer/dam" metaphors — use "builder of resilient local-first systems" instead.
Include caregiver context professionally, not as pity.
Mention: Forge v0.6 (21 connectors), CompuSurf v2.0, Family Guardian MVP, TradeShield.
End with availability for global remote work. Afrikaans closing line optional.)

## Skills to add (comma list)
(8-12 relevant skills)

## Human gate checklist
- [ ] Reviewed for over-promising
- [ ] No private phone numbers
- [ ] Product maturity labels correct
- [ ] Approved for publish

Do NOT invent certificates — use "In progress" only where applicable.
"""

    bridge = GeminiBridge(str(FORGE_ROOT))
    print(bridge.status_message())
    result = bridge.generate(prompt, system=SOVEREIGN_SYSTEM_PROMPT)

    if not result.ok:
        print(f"ERROR: {result.error}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"linkedin_draft_{datetime.now().strftime('%Y%m%d')}.md"
    header = [
        "# PresenceForge — LinkedIn Draft",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "**Human gate:** Review before publishing to LinkedIn",
        "",
    ]
    out.write_text("\n".join(header) + result.text + "\n", encoding="utf-8")
    print(f"\n✅ Draft saved: {out}")
    print("\n--- PREVIEW ---\n")
    print(result.text[:2000])
    if len(result.text) > 2000:
        print("\n... (truncated — see full file)")


if __name__ == "__main__":
    main()