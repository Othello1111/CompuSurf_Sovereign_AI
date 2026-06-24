# Forge Engine Setup (after clone)

Symlinks are not in this repo (machine-specific paths). Run once:

```bash
cd ~/CompuSurf_Sovereign_AI_Mastery_v2   # or your clone path
ln -sf ~/AI_Mastery_Project/connectors forge_connectors
ln -sf ~/AI_Mastery_Project/progress/forge_engine.py scripts/forge_engine.py
```

Requires `~/AI_Mastery_Project` with `.env` for cloud connectors (never commit `.env`).