"""Sovereign Skills Loader — SKILL.md discovery and task matching."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILLS_DIR = PACKAGE_ROOT / "skills"


@dataclass
class Skill:
    name: str
    description: str
    instructions: str
    trigger_keywords: list[str]
    examples: str = ""


class SovereignSkillLoader:
    def __init__(self, skills_dir: str | Path | None = None):
        self.skills_dir = Path(skills_dir or DEFAULT_SKILLS_DIR).expanduser()
        self.skills_dir.mkdir(parents=True, exist_ok=True)
        self.loaded_skills: dict[str, Skill] = {}
        self._load_all_skills()

    def _load_all_skills(self) -> None:
        if not self.skills_dir.exists():
            return
        for skill_folder in sorted(self.skills_dir.iterdir()):
            if skill_folder.is_dir():
                skill_file = skill_folder / "SKILL.md"
                if skill_file.exists():
                    self._parse_skill(skill_folder.name, skill_file)

    def _parse_skill(self, name: str, skill_file: Path) -> None:
        content = skill_file.read_text(encoding="utf-8")
        description = ""
        instructions = ""
        trigger_keywords: list[str] = []
        examples = ""
        current_section: str | None = None

        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("description:"):
                description = stripped.split(":", 1)[1].strip()
            elif stripped.startswith("trigger:"):
                raw = stripped.split(":", 1)[1]
                trigger_keywords = [k.strip() for k in re.split(r"[,;]", raw) if k.strip()]
            elif stripped.lower().startswith("## instructions") or stripped.lower().startswith(
                "## core"
            ):
                current_section = "instructions"
            elif stripped.lower().startswith("## examples"):
                current_section = "examples"
            elif current_section == "instructions":
                instructions += line + "\n"
            elif current_section == "examples":
                examples += line + "\n"

        self.loaded_skills[name] = Skill(
            name=name,
            description=description,
            instructions=instructions.strip(),
            trigger_keywords=trigger_keywords,
            examples=examples.strip(),
        )

    def list_skills(self) -> list[str]:
        return sorted(self.loaded_skills.keys())

    def get_relevant_skills(self, task_description: str, max_skills: int = 5) -> list[Skill]:
        task_lower = task_description.lower()
        scored: list[tuple[int, Skill]] = []

        for skill in self.loaded_skills.values():
            score = 0
            for kw in skill.trigger_keywords:
                if kw.lower() in task_lower:
                    score += 2
            for word in skill.description.lower().split():
                if len(word) > 4 and word in task_lower:
                    score += 1
            if score > 0:
                scored.append((score, skill))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [s[1] for s in scored[:max_skills]]

    def build_context_for_agent(self, task_description: str) -> str:
        relevant = self.get_relevant_skills(task_description)
        if not relevant:
            return ""

        parts = ["\n=== SOVEREIGN SKILLS ACTIVE ==="]
        for skill in relevant:
            parts.append(f"\n[SKILL: {skill.name}]")
            parts.append(f"Description: {skill.description}")
            parts.append(f"Instructions:\n{skill.instructions}")
            if skill.examples:
                parts.append(f"Examples:\n{skill.examples}")
        return "\n".join(parts)
