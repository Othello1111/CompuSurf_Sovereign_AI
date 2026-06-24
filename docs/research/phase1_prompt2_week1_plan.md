# Phase 1 — Prompt 2: GROK.md Validasie + Week 1 Dag-vir-Dag Plan
**Generated:** 21 June 2026 (Sunday) | **For:** Johann Hendrik Reyneke (FalconUnhinged) | **Human gate:** Review before any public changes

---

## 1. GROK.md Validasie

### Wat belyn goed ✅

| Area | Status | Notes |
|------|--------|-------|
| 8-fase v2.0 plan | ✅ Aligned | Section 4 matches dashboard phases 1–8 |
| GCHPP protocol | ✅ Strong | Human gate, structured prompts, sovereign mindset |
| Architecture layers | ✅ Clear | Obsidian → Grok → Intelligence → Execution → Interface → Products |
| Phase 1 ship criteria | ✅ Match | "Professional presence + GROK.md live + first cert in progress" |
| Dashboard workflow | ✅ Present | Daily ritual in Section 6 |
| Confidential classification | ✅ Correct | Personal project files, not public doc |

### Gaps en ouer taal wat aangepas moet word ⚠️

| Gap | Huidige teks | Voorgestelde wysiging | Prioriteit |
|-----|--------------|----------------------|------------|
| **Forge v0.6 integrasie ontbreek** | Geen verwysing na symlink setup | Voeg nuwe subsection onder §3 of §6 | Hoog |
| **Verkeerde CLI pad** | `python progress/forge_engine.py` | `python scripts/forge_engine.py` (vanaf v2 root) | Hoog |
| **Check-up script ontbreek** | Nie genoem | Voeg `scripts/forge_v2_checkup.sh` na weeklikse ritueel | Medium |
| **Publieke posisionering** | "faith-driven boer style", "volk", "Staan op in Jesus Naam" (×3) | Hou in **private** GROK.md; skep aparte `PUBLIC_POSITIONING.md` vir LinkedIn/X | Hoog |
| **Telefoonnommer in konteks** | `0712255007` in §1 WhatsApp line | Verwyder nommer; gebruik "business WhatsApp instance" | Medium (POPIA) |
| **Caregiving framing** | Implisiet maar nie as beperking | Voeg "24/7 caregiving constraint" onder §5 | Medium |
| **Data analysis + Termux** | Nie in architecture | Voeg Forge layers: `--analyze-data`, `--termux sync` | Laag |
| **Neutrale korporatiewe headline** | Nie gedefinieer | Voeg §1.1 Public Positioning Statement | Hoog |

### Voorgestelde klein GROK.md wysigings (diff-styl)

**A. Voeg na §1 (vision) — Public Positioning (copy-paste block vir profiles):**

```markdown
### 1.1 Public Positioning (Neutral · Corporate · International)

**Headline:** Sovereign AI Architect | Local-first agent platforms & self-improving systems

**One-liner:** I build privacy-respecting, self-hosted AI agent harnesses that ship real products — from a caregiver's desk in Pretoria.

**Tone rules for LinkedIn / X / GitHub:** Professional English primary. No faith/boer slang in public bios. Caregiver context = credibility, not pity. Products labelled by maturity (MVP / Alpha / v0.6).
```

**B. Vervang §1 WhatsApp line:**

```diff
- Sovereign WhatsApp layer (Evolution API) for business (0712255007) + family caregiving alerts
+ Sovereign WhatsApp layer (Evolution API) — business instance + family alert channel (numbers in private .env only)
```

**C. Soft §2 item 5 + §5 motivation (keep faith private, professional public):**

```diff
- "Think like a boer building resilient systems for volk and family."
+ "Think like a builder of resilient, local-first systems — practical, durable, family-supporting."

- "Every small ship builds the legacy for your family and the volk."
+ "Every small ship builds capability for family and clients — one repeatable action at a time."
```

**D. Voeg §3.1 Sovereign Forge Integration:**

```markdown
### 3.1 Sovereign Forge Engine v0.6 (Integrated — Do Not Duplicate)

**Location:** `~/AI_Mastery_Project` (source) → symlinked into v2.0:
- `forge_connectors/` → `~/AI_Mastery_Project/connectors/` (20 connectors)
- `scripts/forge_engine.py` → `~/AI_Mastery_Project/progress/forge_engine.py`

**Key CLI (from v2 root, venv active):**
```bash
compusurf   # alias: cd + activate venv
python scripts/forge_engine.py --connectors
python scripts/forge_engine.py --improve --apply   # human gate in script
python scripts/forge_engine.py --analyze-data "topic"
bash scripts/forge_v2_checkup.sh                   # weekly check-up + logging
```

**Status baseline (21 Jun 2026):** 10/20 connectors active. Improve engine operational.
```

**E. Fix §6 step 6:**

```diff
- Run `python progress/forge_engine.py --improve --apply`
+ Run `bash scripts/forge_v2_checkup.sh` (weekly) or `python scripts/forge_engine.py --improve --apply` (ad-hoc)
```

> **Human gate:** Pas bogenoemde wysigings slegs aan nadat jy elke blok goedkeur. Geen outomatiese publikasie.

---

## 2. Week 1 Dag-vir-Dag Uitvoeringsplan

**Periode:** Sondag 21 Jun – Saterdag 27 Jun 2026  
**Tyd-budget:** 30–120 min/dag · ~6–8 uur totaal  
**Fokus:** Phase 1 — Foundation, Research & Online Presence  
**Ritueel:** Dashboard oop → een fokus → human gate → merk milestone → log in Obsidian (opsioneel)

| Dag | Datum | Fokus | Tyd | Spesifieke aksies | Dashboard / Proof |
|-----|-------|-------|-----|-------------------|-------------------|
| **So** | 21 Jun | **Momentum + social proof** | 30–45 min | ① Open dashboard, merk reeds voltooide milestones (GROK.md, prompts, Prompt 1 research). ② `compusurf && python scripts/forge_engine.py --connectors` → screenshot. ③ Stoor screenshot na `00_Overview_and_Tracking/forge_connectors_20260621.png`. ④ Lees PresenceForge copy in `docs/research/phase1_prompt1_market_presenceforge.md` §4 — **draft only**, geen publiseer. | Milestones 0–2 ✓ · ~6–8% overall |
| **Ma** | 22 Jun | **LinkedIn draft (human gate)** | 45–60 min | ① Neem LinkedIn snapshot (screenshot). ② Pas Headline Option A aan (neutral corporate). ③ Draft About — verwyder "boer/dam" vir publieke weergawe; behou caregiver credibility. ④ **Stoor draft** in `docs/research/presenceforge_outputs/linkedin_draft.md`. ⑤ **Moenie publiseer** tot jy goedkeur. | Milestone 3 partial · ~10% |
| **Di** | 23 Jun | **GitHub presence** | 45–60 min | ① Skep/update `FalconUnhinged` profile README (struktuur uit Prompt 1 §4). ② Pin Sovereign Forge repo indien beskikbaar. ③ Voeg connector count + stack badges. ④ Human gate voor "Publish profile". | Milestone 3 ✓ · ~12% |
| **Wo** | 24 Jun | **X strategy + eerste post** | 30–45 min | ① Update X bio (160 chars, neutral). ② Skryf pinned thread outline (5 posts) na `presenceforge_outputs/x_thread_draft.md`. ③ Publiseer **slegs post 1** (hook + screenshot) — indien goedgekeur. | Eerste social proof live · ~13% |
| **Do** | 25 Jun | **Forge check-up + improve cycle** | 60–90 min | ① `bash scripts/forge_v2_checkup.sh` (ja vir improve indien tyd). ② Review `progress/checkup_*.log`. ③ Konfigureer **een** connector (bv. GitHub `.env`) indien sleutel beskikbaar. ④ Tweede social post: connector manifest / improve stats. | Opsioneel Phase 7 milestone 0 · ~14% |
| **Vr** | 26 Jun | **Certificate + case study start** | 45–60 min | ① Begin Anthropic Claude 101 (of Elements of AI) — 1 module. ② Voeg "Certificate in progress" by LinkedIn draft. ③ Begin 1-pager: "Why Sovereign Forge — caregiver builder perspective" (private draft). | Cert in progress noted · ~15% |
| **Sa** | 27 Jun | **Week 1 review + buffer** | 30–60 min | ① Dashboard review: Phase 1 milestones 4/4? Overall ~15%? ② Publiseer LinkedIn **indien** drafts goedgekeur (anders skuif na Week 2). ③ Week 2 micro-focus kies (Phase 2 prep OF LinkedIn finish). ④ Kort Obsidian week-nota. | **Week 1 ship:** presence drafts + 1 social proof · **~15% target** |

### Dashboard progress wiskunde (verwagting)

- **32** milestones totaal + **16** bonus slots (8 fases × 2) = **48** denominator
- **~15%** ≈ **7** completed milestone ticks
- **Week 1 realistic path:**
  - Phase 1: 4/4 milestones (GROK, prompts, research, bio draft) = 4 ticks
  - Optional early ticks: e.g. note Prompt 2 complete, connector screenshot filed, cert started = +2–3
  - **Target Saturday:** 6–8 ticks → **12–17%** (15% is haalbaar)

### As ’n dag korter is (caregiving buffer)

| Skip first | Keep always |
|------------|-------------|
| X posts, cert module | Dashboard tick (1 min) |
| GitHub polish | Forge `--connectors` screenshot (5 min) |
| Improve `--apply` | Human gate review van drafts |

**Geen skuld.** Verskuif na Saterdag-buffer of Week 2 Maandag.

---

## 3. Integrasie Wenke: Obsidian + Dashboard + Forge CLI

### Drie-laag model (moenie alles gelyktydig oop maak nie)

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1 — OBSIDIAN (Ideation · 5–15 min)                   │
│  • Daily note: "Today ONE focus"                            │
│  • Link na GROK.md (symlink of copy in vault root)          │
│  • Paste PresenceForge drafts voor goedkeuring              │
└──────────────────────────┬──────────────────────────────────┘
                           │ human gate
┌──────────────────────────▼──────────────────────────────────┐
│  LAYER 2 — DASHBOARD (Compass · 2–5 min)                    │
│  • file:///.../dashboard.html in browser bookmark           │
│  • Tick ONE milestone per session                           │
│  • localStorage = permanent if opened via file://           │
└──────────────────────────┬──────────────────────────────────┘
                           │ execute
┌──────────────────────────▼──────────────────────────────────┐
│  LAYER 3 — TERMINAL / FORGE CLI (Action · 15–60 min)        │
│  • compusurf → venv + correct directory                     │
│  • forge_engine.py --connectors | --improve | --analyze-data  │
│  • forge_v2_checkup.sh weekly (Donderdag aanbeveel)        │
└─────────────────────────────────────────────────────────────┘
```

### Praktiese setup (eenmalig, ~20 min — enige dag hierdie week)

1. **Obsidian vault:** Symlink `GROK.md` en `dashboard.html` into vault root:
   ```bash
   ln -sf ~/CompuSurf_Sovereign_AI_Mastery_v2/00_Overview_and_Tracking/GROK.md ~/path/to/vault/GROK.md
   ```
2. **Dashboard bookmark:** `file:///home/falconunhinged/CompuSurf_Sovereign_AI_Mastery_v2/00_Overview_and_Tracking/dashboard.html`
3. **Terminal alias:** Reeds in `~/.bashrc`: `compusurf`
4. **Daily note template** (Obsidian):
   ```markdown
   ## CompuSurf · {{date}}
   - [ ] Dashboard oop + 1 milestone
   - [ ] Forge: connectors / check-up / improve
   - Focus: Phase 1 — ___
   - Human gate: ___
   - Caregiving note: (kort dag indien nodig)
   ```

### Anti-overwhelm reëls

| Reël | Waarom |
|------|--------|
| **Een venster per sessie** | Obsidian OF terminal OF LinkedIn — nie al drie |
| **Max 2 Forge commands per dag** | `--connectors` + een ander |
| **Drafts in `docs/research/`** | Nie in Obsidian én GitHub én LinkedIn gelyktydig redigeer nie |
| **Vrydag = geen nuwe tools** | Slegs review + buffer |
| **Check-up script = Donderdag** | Vaste ritueel; reduce decision fatigue |

### VSCode / Cursor integrasie

- Open workspace root: `~/CompuSurf_Sovereign_AI_Mastery_v2`
- Terminal panel: `compusurf` voor enige Forge run
- Side-by-side: `dashboard.html` preview + `presenceforge_outputs/` drafts

---

## 4. Vandag se Eenvoudigste Volgende Stap (Sondag 21 Jun)

### Hoogste impak · laagste wrywing (30 min)

```bash
compusurf
python scripts/forge_engine.py --connectors
```

1. **Screenshot** die connector-tabel (10/20 active = social proof)
2. **Stoor** as `00_Overview_and_Tracking/forge_connectors_20260621.png`
3. **Open dashboard** → merk milestones:
   - ✅ GROK.md template created & populated
   - ✅ Phase 1 GCHPP prompts ready
   - ✅ Market research completed
4. **Moenie** nog LinkedIn publiseer — lees net §4 van Prompt 1 research

### Verwagte dashboard progress na vandag

| Metriek | Waarde |
|---------|--------|
| Phase 1 milestones | 3/4 (75%) |
| Overall progress | **~6–8%** |
| Tangible artifact | Connector screenshot (eerste social proof) |
| Volgende human gate | Maandag LinkedIn draft |

---

## 5. Risiko's en Mitigasie

| Risiko | Impak | Mitigasie |
|--------|-------|-----------|
| **Caregiving nood laat geen sessie toe** | Week 1 slip | 5-min dashboard tick + screenshot only; buffer Saterdag |
| **Te veel "boer/faith" in publieke copy** | Korporatiewe kliënte afskrik | Gebruik `PUBLIC_POSITIONING.md` / Prompt 1 Option A; faith bly privaat |
| **Oor-beloof onvoltooide produkte** | Trust verloor | Label altyd: v0.6, MVP, Alpha, In Progress |
| **Human gate oorgeslaan** | Verkeerde publieke pos | Geen auto-publish; drafts in `presenceforge_outputs/` |
| **Dashboard progress reset** | Demotiverend | Open via `file://` vir localStorage; backup weekly screenshot |
| **Forge improve wysig verkeerde lêers** | Project break | Check-up script vra bevestiging; review `progress/improve_log.json` |
| **llava / Playwright nog nie** | Phase 2 block later | Nie Week 1 scope; retry wanneer netwerk stabiel |
| **POPIA / familie data** | Legal + trust | Geen regte nommers in GROK.md; synthetic demos only |
| **Connector 10/20 lyk "half done"** | Weak social proof | Frame as "local-first core active; cloud optional" |
| **Rabbit hole: Phase 2 Crawl4AI** | Week 1 mis | Dashboard guardrail: "FOCUS Phase 1" button |

---

## 6. Week 1 Definition of Done (Ship Criteria)

Phase 1 is **Week 1 ready** (nie volledig complete nie) wanneer:

- [x] GROK.md validated + klein wysigings goedgekeur (hierdie dokument)
- [ ] LinkedIn + GitHub drafts goedgekeur (publikasie human gate)
- [ ] Minstens **1** publieke social proof (connector screenshot op X of LinkedIn)
- [ ] Dashboard **≥15%** overall
- [ ] `forge_v2_checkup.sh` minstens 1× gedraai met log
- [ ] Certificate enrolment gestart

**Week 2 preview:** LinkedIn publish · GitHub README live · Phase 2 Crawl4AI install test · PresenceForge snapshot audit met regte profile screenshots.

---

*DeepFlow × Sovereign Forge — Phase 1 GCHPP Prompt 2 complete. Human gate before all public actions.*