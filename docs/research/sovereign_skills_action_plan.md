# SovereignSkills + HermesGraph — Integration & Schedule Plan
**Date:** 22 June 2026 | **Status:** Foundation integrated | **Human gate:** All public/on-chain actions

---

## Executive Summary

Two trending concepts mapped to CompuSurf stack:

| Concept | Source inspiration | Sovereign implementation |
|---------|-------------------|-------------------------|
| Agent subcontract + escrow | OpenHuman / x402 | `sovereign_skills/marketplace/` — **internal credits ledger** (no chain yet) |
| Skills + Memory Graph | kingwilliam_ pattern | `sovereign_skills/skills/` + `memory_graph/hermes_graph.py` |

**Not building today:** Solana, USDC, on-chain escrow — Phase 6+ optional module.

---

## What Was Integrated (22 Jun 2026)

```
CompuSurf_Sovereign_AI_Mastery_v2/sovereign_skills/
├── core/skill_loader.py          # SKILL.md loader + keyword match
├── memory_graph/hermes_graph.py  # Persistent graph (networkx + JSON)
├── marketplace/agent_economy.py  # Internal job ledger
├── skills/
│   ├── trading/SKILL.md
│   ├── family_care/SKILL.md
│   ├── forge_build/SKILL.md
│   └── presence/SKILL.md
├── data/                         # Auto-created: graph + economy JSON
└── examples/                     # (Phase 4)

scripts/sovereign_agent.py        # CLI: --task, --status, --seed-graph, --run
```

**Forge integration:** `sovereign_agent.py` routes to Ollama (default) or Gemini via existing `agents/gemini_bridge.py`.

---

## Schedule Adjustment (LinkedIn blocked)

| Original Week 1 | Adjusted | Reason |
|-----------------|----------|--------|
| LinkedIn publish | **DEFERRED** — draft ready | Profile recovery pending |
| Phase 1 presence | GitHub README + X draft instead | No LinkedIn dependency |
| Phase 4 Jarvis | **Start foundation early** | SovereignSkills = Layer 2.5 |

### Revised Week 1 (remaining days)

| Day | Focus | Time | Ship |
|-----|-------|------|------|
| **22 Jun** | SovereignSkills integration | 45 min | ✅ CLI + 7 skills + graph seed |
| **22 Jun** | GitHub README | 30 min | ✅ `README.md` + profile variant |
| **Next** | Push repo to GitHub + pin | 30 min | Public presence live |
| **When LinkedIn recovers** | Paste `linkedin_final_copypaste.md` | 20 min | Phase 1 milestone |
| **This week** | Migrate skills from legacy `~/compusurf/openclaw/` | 60 min | Reuse old work safely |

**Phase 1 ship criteria (adjusted):**
- [x] GROK.md live
- [x] Market research complete
- [x] Presence drafts ready
- [ ] **Any 2 of:** LinkedIn live OR GitHub README OR first X post

---

## CLI Quick Reference

```bash
compusurf

# Status
python scripts/sovereign_agent.py --status

# Seed graph (once)
python scripts/sovereign_agent.py --seed-graph

# Build context only (no LLM cost)
python scripts/sovereign_agent.py --task "Improve TradeShield logging"

# Run with local Ollama
python scripts/sovereign_agent.py --task "..." --run --provider ollama

# Run with Gemini (complex / public copy)
python scripts/sovereign_agent.py --task "..." --run --provider gemini
```

---

## Phase Roadmap (SovereignSkills in 8-phase plan)

| Phase | SovereignSkills milestone |
|-------|---------------------------|
| **1** (now) | 4 core skills + graph seed + CLI |
| **2** | Crawl4AI feeds graph with research nodes |
| **3** | WhatsApp alerts write to graph (caregiving events) |
| **4** | Full Jarvis pipeline: task → skills → graph → agent → human gate |
| **5** | Family Guardian reads/writes graph (meds, appointments) |
| **6** | Agent marketplace: real subcontract between Forge agents |
| **7** | Trading agents post/claim jobs via economy layer |
| **8** | Optional: x402/Solana bridge (separate module, human gate) |

---

## Risks & Mitigation

| Risk | Mitigation |
|------|------------|
| Scope creep (OpenHuman clone) | Internal credits only until Phase 6 |
| Graph grows messy | Node types enforced; weekly graph review |
| Skill overload | Max 5 skills injected per task |
| Legacy `~/compusurf/openclaw` confusion | Migrate selectively; archive rest later |
| RAM pressure for Ollama | `ollama stop gemma3n`; use Gemini for heavy tasks |

---

## Next Actions (priority order)

1. **Test:** `python scripts/sovereign_agent.py --status`
2. **Test:** One real task with `--run --provider gemini`
3. **Add skill:** `sovereign_skills/skills/content/SKILL.md` for your content workflow
4. **GitHub README** while LinkedIn blocked
5. **LinkedIn publish** when profile recovered — draft unchanged in `presenceforge_outputs/`

---

*Integrated with Sovereign Forge v0.6 + CompuSurf v2.0 — local-first, human-gated.*