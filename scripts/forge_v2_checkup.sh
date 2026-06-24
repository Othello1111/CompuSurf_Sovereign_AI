#!/bin/bash
###############################################################################
# Forge + CompuSurf v2.0 Daily/Weekly Check-up Script
# Doel: Volledige status + self-improvement run met veilige human gate
###############################################################################

set -e

PROJECT_DIR="$HOME/CompuSurf_Sovereign_AI_Mastery_v2"
LOG_DIR="$PROJECT_DIR/progress"
LOG_FILE="$LOG_DIR/checkup_$(date '+%Y%m%d_%H%M%S').log"
cd "$PROJECT_DIR"
mkdir -p "$LOG_DIR"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║     COMPUSURF SOVEREIGN AI MASTERY v2.0  +  FORGE ENGINE CHECK-UP         ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Datum & Tyd: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Projek: $PROJECT_DIR"
echo "Log: $LOG_FILE"
echo ""

# === 1. Aktiveer omgewing ===
echo ">>> [1/6] Aktiveer venv en Forge integrasie..."
source .venv/bin/activate
echo "Venv aktief: $(which python3)"

# === 2. Forge Connector Status ===
echo ""
echo ">>> [2/6] Forge Connector Status (via symlink)..."
echo "──────────────────────────────────────────────────────────────────────────────"
python scripts/forge_engine.py --connectors 2>/dev/null || echo "⚠️  forge_engine.py nie gevind of fout nie"

# === 3. Projek Struktuur + Sleutel Lêers ===
echo ""
echo ">>> [3/6] Projek Struktuur + Sleutel Lêers..."
echo "──────────────────────────────────────────────────────────────────────────────"
echo "Forge symlink status:"
ls -ld forge_connectors 2>/dev/null || echo "forge_connectors symlink nie gevind nie"
ls -l scripts/forge_engine.py 2>/dev/null || echo "forge_engine.py symlink nie gevind nie"

echo ""
echo "Kern lêers in 00_Overview_and_Tracking/:"
ls -1 00_Overview_and_Tracking/ 2>/dev/null | head -10

echo ""
echo "Prompts beskikbaar:"
ls -1 prompts/ 2>/dev/null

# === 4. Ollama Modelle ===
echo ""
echo ">>> [4/6] Ollama Modelle Status..."
echo "──────────────────────────────────────────────────────────────────────────────"
ollama list 2>/dev/null || echo "⚠️  Ollama nie bereikbaar nie"

# === 5. Self-Improvement Engine (met human gate) ===
echo ""
echo ">>> [5/6] Self-Improvement Engine Run"
echo "──────────────────────────────────────────────────────────────────────────────"
echo "Die Self-Improvement Engine gaan nou die hele projek analiseer en veilige"
echo "wysigings voorstel / toepas (documentation, code quality, gaps, ens.)."
echo ""
read -p "Wil jy --improve --apply nou hardloop? (ja/nee): " CONFIRM

if [[ "$CONFIRM" == "ja" || "$CONFIRM" == "y" || "$CONFIRM" == "Y" ]]; then
    echo ""
    echo ">>> Running: python scripts/forge_engine.py --improve --apply"
    python scripts/forge_engine.py --improve --apply
    echo ""
    echo "✅ Improve run voltooi. Kyk na progress/improve_log.json vir details."
else
    echo "⏭️  Improve run oorgeslaan (dry-run modus). Jy kan dit later self hardloop."
fi

# === 6. Dashboard & Progress Snapshot ===
echo ""
echo ">>> [6/6] Dashboard & Progress Snapshot..."
echo "──────────────────────────────────────────────────────────────────────────────"
if [ -f "00_Overview_and_Tracking/dashboard.html" ]; then
    echo "✅ dashboard.html bestaan en is gereed vir gebruik in browser."
else
    echo "⚠️  dashboard.html nie gevind nie."
fi

if [ -f "00_Overview_and_Tracking/GROK.md" ]; then
    echo "✅ GROK.md bestaan."
else
    echo "⚠️  GROK.md nie gevind nie."
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                           CHECK-UP KLAAR                                   ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Volgende aanbevole aksies:"
echo "1. Maak dashboard.html oop in browser en tik enige nuwe milestones af."
echo "2. As improve run gedoen is → commit die klein wysigings."
echo "3. Stuur die volledige uitset van hierdie script na Grok vir ontleding."
echo ""
echo "Staan op in Jesus Naam. Small consistent ships."