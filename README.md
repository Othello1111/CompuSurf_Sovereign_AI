# CompuSurf • Sovereign AI Infrastructure

**Local-first agentic systems for builders who refuse cloud lock-in.**

CompuSurf ships sovereign AI tools that run on your hardware, respect privacy, and improve over time — with persistent memory and skills that survive every session.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED)
![Ollama](https://img.shields.io/badge/Ollama-local_first-black)
![Status](https://img.shields.io/badge/Phase-4_Foundation-green)

## Current Focus (June 2026)

### SovereignSkills + HermesGraph

Local implementation of **persistent memory graphs** + **automatic skills loading** — the missing layer between Forge execution and long-running agent context.

| Module | Status | Description |
|--------|--------|-------------|
| **HermesGraph** | Foundation live | Directed graph: projects, decisions, tasks, skills — JSON on disk |
| **SovereignSkills** | 4+ skills active | `SKILL.md` auto-match per task (trading, care, forge, presence) |
| **Agent Economy** | Foundation live | Internal credits ledger for agent subcontract (on-chain x402 later) |

```bash
compusurf
python scripts/sovereign_agent.py --status
python scripts/sovereign_agent.py --task "Your task" --run --provider gemini
```

### Sovereign Forge Engine v0.6

21-connector agent harness with self-improvement, hybrid routing (Ollama → Gemini → Claude), and manifest-driven architecture.

```bash
python scripts/forge_engine.py --connectors
python scripts/forge_engine.py --sovereign-hybrid --task "Week plan"
```

## Core Stack

| Layer | Component | Status |
|-------|-----------|--------|
| Memory & Context | HermesGraph | Foundation live |
| Agent Behaviour | SovereignSkills | Active |
| Coordination | Agent Economy | Foundation live |
| Execution | Sovereign Forge v0.6 | v0.6 ✅ |
| Orchestration | OpenClaw + Guardian OS | Active (ecosystem) |
| Trading | TradeShield / Quantum Edge | In Progress |
| Local LLM | Ollama + optional Gemini API | Active |

## Philosophy

- **Sovereign by default** — Local-first. Cloud is optional, never required.
- **Memory that survives sessions** — Graph + skills inject real context; no re-explaining every chat.
- **Agents that collaborate** — Subcontract tasks with internal ledger and human gate.
- **Built for real constraints** — Offline-capable, load-shedding resilient, POPIA-aware design.

## Projects

| Project | Description | Maturity |
|---------|-------------|----------|
| **Sovereign Forge** | 21-connector harness + improve engine | v0.6 |
| **CompuSurf v2.0** | 8-phase mastery program | Active |
| **Family Guardian** | Caregiver-first home automation | MVP |
| **TradeShield** | Privacy-first trading intelligence | Alpha |
| **OpenClaw / Hermes** | Agent framework + cognitive layer | Ecosystem |

## Repository Structure

```
CompuSurf_Sovereign_AI_Mastery_v2/
├── sovereign_skills/       # Skills + HermesGraph + Agent Economy
├── scripts/                # sovereign_agent.py, forge_engine.py (symlink)
├── 00_Overview_and_Tracking/  # GROK.md, dashboard.html
├── docs/research/          # Plans, PresenceForge outputs
└── forge_connectors/       # Symlink → AI_Mastery_Project
```

## Tech

Python 3.13 • Docker • NetworkX • LangGraph • Crawl4AI • Ollama • Gemini (API, human-gated) • Ubuntu

## Roadmap

- **Phase 1** — Foundation + presence (in progress; LinkedIn pending recovery)
- **Phase 2** — Hybrid Web Intelligence (Crawl4AI)
- **Phase 3** — Self-hosted knowledge + WhatsApp layer
- **Phase 4** — SovereignSkills + Jarvis pipeline ← **current foundation**
- **Phase 6+** — Optional x402 / USDC agent economy bridge

## Why This Matters

Most AI tools reset every conversation. Most multi-agent platforms require cloud accounts and export your data.

CompuSurf builds the opposite: agents that remember your projects, respect your privacy, and coordinate with clear human gates.

## Get Involved

- **Remote contract work** — Sovereign AI architecture, agent harnesses, automation (Pretoria → global)
- **White-label agents** — Local-first systems for business or community use
- **Collaboration** — Builders working on privacy-respecting, offline-capable AI in emerging markets

Open an issue or DM via GitHub.

---

**Pretoria, South Africa** · English & Afrikaans · Built for resilience, not hype.