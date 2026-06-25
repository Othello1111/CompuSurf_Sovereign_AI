# GROK.md - CompuSurf Sovereign AI Global Mastery v2.0 Root Context

**Project:** CompuSurf IT Solutions - Sovereign AI Global Mastery Program v2.0  
**Owner:** Johann Hendrik Reyneke (FalconUnhinged) / CompuSurf IT Solutions  
**Date:** 21 June 2026  
**Version:** 2.0 - Finalized after Orchestrator Review  
**Classification:** Confidential - Personal Project Files  
**Core Philosophy:** Learn → Build Small → Ship → Repeat. Use DeepFlow + Grok to research, scaffold and execute while shipping real sovereign products with global demand.

---

## 1. PROJECT VISION & STRATEGIC OBJECTIVES (Next 8-12 Weeks)

This is your single source of truth. Integrate cutting-edge open-source tools, advanced Grok-Claude Hybrid Prompting Protocol (GCHPP), and a practical Grok-orchestrated execution pipeline.

### 1.1 Public Positioning (LinkedIn, X, GitHub, Website)

**Recommended public headline:**
Sovereign AI Architect | Local-first agent platforms & self-improving systems | Forge Engine • Guardian OS | Builder · Pretoria

**Tone guidance:**
- Public profiles: Neutral, professional, corporate-friendly, internationally appealing.
- Private/internal documents (GROK.md, prompts, Obsidian): May include personal faith, heritage, and family context.
- Avoid mixing the two. Keep "boer/volk" framing for private notes and faith-based content only.

**Ship 3-4 production-ready sovereign products:**
- Family Guardian Agent (local-first for aging population care - $67B+ market)
- Sovereign DataForge
- Enhanced Trading Intelligence (Quantum Edge / TradeShield)
- CompuSurf Sovereign Toolkit bundle

**Establish professional global online presence:**
- Cleaned LinkedIn, GitHub portfolio, X strategy
- Recognized certificates (HF Agents, n8n, Elements of AI)

**Build & integrate:**
- Hybrid Web Intelligence layer (Crawl4AI/Firecrawl/Scrapling + PixelRAG vision fallback)
- Sovereign WhatsApp layer (Evolution API) — dual instances for business and private use (numbers in private `.env` only)
- Grok-powered Jarvis execution pipeline with human gate (blood-brain barrier) between Obsidian ideation and Ubuntu/Docker execution

**Unlock advanced agentic skills** through custom GCHPP tailored to your sovereign, truth-seeking, practical, faith-driven boer style.

---

## 2. GCHPP - GROK-CLAUDE HYBRID PROMPTING PROTOCOL (Core Principles)

Use these ALWAYS when prompting Grok/DeepFlow:

1. **Structured Sections:** XML-style or clear Markdown: <context>, <task>, <tools>, <constraints>, <examples>, <output_format>.

2. **Tool Schema Excellence:** Define every tool with: purpose (1 sentence), exact parameters + types, when to use vs NOT use, success/failure examples.

3. **Long-Context Discipline:** Put long documents/data at the TOP. Use <document> tags with metadata. Queries at the end.

4. **Human Gate (Blood-Brain Barrier):** EVERY execution pipeline MUST include explicit human approval step before any file changes, deployments, or external actions.

5. **Sovereign Mindset Injection:** "Prioritize local-first, offline-capable, privacy-respecting solutions. Avoid cloud APIs where possible. Think like a boer building resilient systems for volk and family."

6. **DeepFlow Sub-Agent Spawning:** Break complex tasks into sub-agents with clear handoffs (research agent → scaffold agent → review agent).

7. **Truth + Practicality:** Direct feedback, identify risks honestly, suggest simplest viable path first, then iterate.

8. **Few-Shot + Examples:** Provide 1-2 concrete examples of desired output format or successful previous runs.

**Result:** Faster, more reliable agent building, better long-term architecture, prompting style that feels like extension of your practical, faith-driven, sovereign thinking. Staan op in Jesus Naam.

---

## 3. INTEGRATED ARCHITECTURE LAYERS

- **Layer 1 - Ideation:** Obsidian Vault → GROK.md root context
- **Layer 2 - Orchestration:** Grok (this) + DeepFlow SuperAgent Harness (sub-agents, memory, sandbox, skills)
- **Layer 3 - Intelligence:** Hybrid Web Tool (Crawl4AI primary + PixelRAG fallback) + Self-Hosted Toolkit (Stirling-PDF, Open Notebook, Excalidraw, Recordly)
- **Layer 4 - Execution:** Python/Docker workers + Guardian OS self-healing + OpenClaw agents
- **Layer 5 - Interface:** WhatsApp Sovereign Layer (Evolution API dual instances) + Terminal/UI human gate
- **Layer 6 - Products:** Family Guardian Agent, Sovereign DataForge, Trading Intelligence, CompuSurf Toolkit

**Key Tool Integration Priority:** Web Intelligence (*****), Document & Knowledge (*****), Orchestration (*****), Communication (****), Visual & Planning (****), Trading (****)

### 3.1 Sovereign Forge Engine Integration (v0.6)

The existing **Sovereign Forge Engine v0.6** (in `~/AI_Mastery_Project`) is integrated into this v2.0 project via symlinks:

- `forge_connectors/` → `~/AI_Mastery_Project/connectors`
- `scripts/forge_engine.py` → improve engine + connector registry
- Daily/weekly check-up: `./scripts/forge_v2_checkup.sh`

This integration provides access to 20 connectors, the self-improvement engine, registry, and `manifest.json` without duplicating the mature Forge project.

```bash
compusurf
python scripts/forge_engine.py --connectors
python scripts/forge_engine.py --improve --apply
```

### 3.2 SovereignSkills + HermesGraph (Agent Memory Layer)

Local-first implementation of **Skills + Memory Graph** (inspired by persistent agent context patterns) and **internal agent marketplace** (inspired by subcontract/escrow patterns — on-chain deferred to Phase 6+).

**Location:** `sovereign_skills/` in this v2.0 project

| Module | Purpose |
|--------|---------|
| `core/skill_loader.py` | Loads `SKILL.md` files; auto-matches tasks |
| `memory_graph/hermes_graph.py` | Persistent graph (projects, decisions, people, tasks) |
| `marketplace/agent_economy.py` | Internal credits ledger for agent subcontract |
| `scripts/sovereign_agent.py` | CLI: inject skills + graph → Ollama or Gemini |

```bash
python scripts/sovereign_agent.py --status
python scripts/sovereign_agent.py --seed-graph
python scripts/sovereign_agent.py --task "Your task" --run --provider gemini
```

**Rules:** Human gate before publish/on-chain. Max 5 skills per task. Graph data stays local in `sovereign_skills/data/`.

Full plan: `docs/research/sovereign_skills_action_plan.md`

### 3.3 Sovereign CI (GitHub Actions — No LLM, No Cloud APIs)

Free quality gate on every push/PR. Protects skills, graph, and Python integrity.

| Workflow | Purpose |
|----------|---------|
| `validate-skills-graph.yml` | 7+ skills load, HermesGraph seeds, agent imports |
| `update-skills-inventory.yml` | Auto-regenerate `docs/SKILLS_INVENTORY.md` |
| `ruff-sovereign-lint.yml` | Lint + format (E, F, I rules via `pyproject.toml`) |

```bash
python scripts/validate_sovereign_skills.py   # same as CI
ruff check . && ruff format --check .
```

**Repo:** https://github.com/Othello1111/CompuSurf_Sovereign_AI  
**Rules:** No secrets in repo. No LLM calls in CI. Human gate before public profile changes.

---

## 4. 8-PHASE MASTER IMPLEMENTATION PLAN (Summary)

**Phase 1 (Week 1):** Foundation, Research & Online Presence Restructuring  
**Ship:** Updated professional online presence + first certificate in progress + GROK.md live

**Phase 2 (Weeks 2-3):** Hybrid Web Intelligence Layer  
**Ship:** Production-ready Hybrid Web Tool + documentation

**Phase 3 (Weeks 3-5):** Self-Hosted Knowledge Toolkit + WhatsApp Layer  
**Ship:** Sovereign document processing + WhatsApp automation live (business + family alerts)

**Phase 4 (Weeks 5-7):** Grok-Powered Jarvis Execution Pipeline  
**Ship:** Jarvis pipeline handling real tasks with your oversight (human gate)

**Phase 5 (Weeks 6-7):** Family Guardian Agent MVP ★ HIGH GLOBAL VALUE  
**Ship:** Shippable Family Guardian Agent prototype (local-first, privacy-first)

**Phase 6 (Weeks 7-9):** Productization & First Monetization Experiments  
**Ship:** First revenue experiment + professional product packaging

**Phase 7 (Weeks 8-10):** Trading Intelligence + Self-Improvement Loop  
**Ship:** Measurably better trading agents + automated self-improvement running

**Phase 8 (Ongoing from Week 6):** Portfolio, Certificates & Global Positioning  
**Ship:** Strong professional brand ready for global freelance/clients + 3+ certificates

**3/6/12 Month Vision:**
- 3 Months: Hybrid Web live • WhatsApp dual • 2 agents shipped • Professional presence • First certificates
- 6 Months: Revenue from Sovereign DataForge or Family Guardian • Jarvis mature • Trading enhanced • Toolkit v1
- 12 Months: Multiple revenue streams • White-label clients • Open-source/paid sovereign tools • Strong global brand in sovereign AI for privacy & resilience

---

## 5. CURRENT STATUS & HUMAN GATE

**This dashboard + GROK.md is your compass.** Before any deep dive or rabbit hole: Open this dashboard first. Tick progress. See the bigger picture. Then choose ONE phase to focus.

**Always include in prompts:** "Apply full GCHPP protocol. Human gate required before any execution or file changes. Sovereign boer mindset: local-first, family-supporting, faith-aligned, practical."

**Motivation:** Every small ship builds capability for family and clients — one repeatable action at a time. DeepFlow and I carry the cognitive load. You focus on high-value decisions and 24/7 caregiving.

Caregiving responsibilities take priority. All planning assumes maximum 1–2 focused hours per day. The system is designed to carry cognitive load so high-value decisions and family time remain protected.

**Staan op in Jesus Naam. Ons bou hierdie saam — prakties, sovereign, en met langtermyn impak.**

---

## 6. HOW TO USE THIS SYSTEM (Daily Workflow)

1. Open `00_Overview_and_Tracking/dashboard.html` (visual tracker) in browser.
2. Check current progress, tick completed items.
3. Read relevant section in GROK.md or phase folder.
4. Use GCHPP prompts from `prompts/` folder.
5. Work in ONE phase only until ship criteria met.
6. Run `./scripts/forge_v2_checkup.sh` or `python scripts/forge_engine.py --improve --apply` for self-improvement (Forge Engine is symlinked).
7. Update dashboard and commit small wins.

**File this in Obsidian Vault root for instant access. Symlink or copy key files to VSCode workspace.**

---

*Document generated with Grok orchestration • Ready for implementation • Confidential to Johann Reyneke / CompuSurf IT Solutions*