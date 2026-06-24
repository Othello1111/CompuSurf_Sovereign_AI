#!/usr/bin/env python3
"""CI/local validation for SovereignSkills + HermesGraph."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

MIN_SKILLS = 5


def validate_skills() -> int:
    from sovereign_skills.core.skill_loader import SovereignSkillLoader

    loader = SovereignSkillLoader()
    count = len(loader.loaded_skills)
    print(f"✅ Skills loaded: {count}")
    for name in loader.list_skills():
        skill = loader.loaded_skills[name]
        if not skill.description or not skill.trigger_keywords:
            print(f"❌ Skill '{name}' missing description or trigger keywords")
            return 1
        print(f"   - {name}")
    if count < MIN_SKILLS:
        print(f"❌ Expected at least {MIN_SKILLS} skills, got {count}")
        return 1
    return 0


def validate_graph() -> int:
    from sovereign_skills.memory_graph.hermes_graph import HermesGraph

    with tempfile.TemporaryDirectory() as tmpdir:
        graph_path = Path(tmpdir) / "test_graph.json"
        graph = HermesGraph(graph_path=graph_path)
        graph.seed_v2_baseline()
        summary = graph.summary()
        print("✅ HermesGraph seeded in temp path")
        print(f"   Nodes: {summary['nodes']}")
        print(f"   Edges: {summary['edges']}")
        if summary["nodes"] < 5:
            print("❌ Graph seed produced too few nodes")
            return 1
    return 0


def validate_agent_import() -> int:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "sovereign_agent",
        ROOT / "scripts" / "sovereign_agent.py",
    )
    if spec is None or spec.loader is None:
        print("❌ Could not load sovereign_agent.py spec")
        return 1
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        print(f"❌ sovereign_agent.py import error: {exc}")
        return 1
    print("✅ sovereign_agent.py imports cleanly")
    return 0


def main() -> int:
    print("=== SovereignSkills CI Validation ===")
    checks = [
        ("skills", validate_skills),
        ("graph", validate_graph),
        ("agent", validate_agent_import),
    ]
    failed = 0
    for name, fn in checks:
        print(f"\n--- {name} ---")
        if fn() != 0:
            failed += 1
    print("\n=== Summary ===")
    if failed:
        print(f"❌ {failed} check(s) failed")
        return 1
    print("✅ All checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
