# CompuSurf • Sovereign AI Infrastructure

**Local-first agentic systems for builders who refuse cloud lock-in.**

CompuSurf ships sovereign AI tools that run on your hardware, respect privacy, and improve over time — with persistent memory and skills that survive every session.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED)
![Ollama](https://img.shields.io/badge/Ollama-local_first-black)
![Status](https://img.shields.io/badge/Phase-4_Foundation-green)
![CI](https://github.com/Othello1111/CompuSurf_Sovereign_AI/actions/workflows/validate-skills-graph.yml/badge.svg)

## Current Focus (June 2026)

### SovereignSkills + HermesGraph

Local implementation of **persistent memory graphs** + **automatic skills loading** — the missing layer between Forge execution and long-running agent context.

| Module | Status | Description |
|--------|--------|-------------|
| **HermesGraph** | Foundation live | Directed graph: projects, decisions, tasks, skills — JSON on disk |
| **SovereignSkills** | 7 skills active | `SKILL.md` auto-match per task |
| **Agent Economy** | Foundation live | Internal credits ledger for agent subcontract (on-chain x402 later) |

```bash
compusurf
python scripts/sovereign_agent.py --status
python scripts/validate_sovereign_skills.py   # same check as GitHub Actions
```

See `docs/SKILLS_INVENTORY.md` for auto-generated skill list.

### Sovereign Forge Engine v0.6

21-connector agent harness with self-improvement and hybrid routing (Ollama → Gemini → Claude).

## CI / Quality

- **validate-skills-graph.yml** — runs on every push (no LLM calls)
- **update-skills-inventory.yml** — refreshes `docs/SKILLS_INVENTORY.md` when skills change

## Philosophy

- **Sovereign by default** — Local-first. Cloud is optional.
- **Memory that survives sessions** — Graph + skills inject real context.
- **Human gate** — No auto-publish, no secrets in repo.

## Get Involved

Remote contract work · White-label agents · Collaboration on local-first AI

---

**Pretoria, South Africa** · English & Afrikaans
