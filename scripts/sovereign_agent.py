#!/usr/bin/env python3
"""
Sovereign Agent CLI — Skills + HermesGraph + optional Forge LLM routing.

Usage:
  python scripts/sovereign_agent.py --task "Fix TradeShield logging"
  python scripts/sovereign_agent.py --task "..." --run --provider gemini
  python scripts/sovereign_agent.py --status
  python scripts/sovereign_agent.py --seed-graph
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parents[1]
FORGE_ROOT = Path.home() / "AI_Mastery_Project"
sys.path.insert(0, str(V2_ROOT))
sys.path.insert(0, str(FORGE_ROOT))

from sovereign_skills.core.skill_loader import SovereignSkillLoader  # noqa: E402
from sovereign_skills.memory_graph.hermes_graph import HermesGraph  # noqa: E402
from sovereign_skills.marketplace.agent_economy import AgentEconomy  # noqa: E402


def build_prompt(task: str) -> str:
    skills = SovereignSkillLoader()
    graph = HermesGraph()
    graph.seed_v2_baseline()

    skills_ctx = skills.build_context_for_agent(task)
    graph_ctx = graph.get_relevant_context(task)
    matched = [s.name for s in skills.get_relevant_skills(task)]

    return f"""{skills_ctx}
{graph_ctx}

=== CURRENT TASK ===
{task}

Matched skills: {', '.join(matched) if matched else 'none'}
Respond with: analysis, risks, and 3 concrete next steps.
"""


def run_llm(prompt: str, provider: str) -> str:
    if provider == "gemini":
        from agents.gemini_bridge import GeminiBridge

        bridge = GeminiBridge(str(FORGE_ROOT))
        result = bridge.generate(prompt)
        if not result.ok:
            raise RuntimeError(result.error or "Gemini failed")
        return result.text

    from agents.base import get_ollama_response

    return get_ollama_response(prompt, model="llama3.2:latest", timeout=120)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sovereign Agent — Skills + Graph")
    parser.add_argument("--task", type=str, help="Task description")
    parser.add_argument("--run", action="store_true", help="Execute via LLM (human gate on actions)")
    parser.add_argument("--provider", choices=["ollama", "gemini"], default="ollama")
    parser.add_argument("--status", action="store_true", help="Show skills/graph/economy status")
    parser.add_argument("--seed-graph", action="store_true", help="Seed HermesGraph baseline nodes")
    args = parser.parse_args()

    if args.seed_graph:
        graph = HermesGraph()
        graph.seed_v2_baseline()
        print(f"✅ Graph seeded: {graph.summary()}")
        return

    if args.status:
        skills = SovereignSkillLoader()
        graph = HermesGraph()
        economy = AgentEconomy()
        print("=== SovereignSkills Status ===")
        print(f"Skills loaded: {skills.list_skills()}")
        print(f"Graph: {graph.summary()}")
        print(f"Economy agents: {len(economy.agents)} | jobs: {len(economy.jobs)}")
        return

    if not args.task:
        parser.print_help()
        sys.exit(1)

    prompt = build_prompt(args.task)
    print(prompt)

    if args.run:
        print("\n=== LLM RESPONSE ===\n")
        try:
            print(run_llm(prompt, args.provider))
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()