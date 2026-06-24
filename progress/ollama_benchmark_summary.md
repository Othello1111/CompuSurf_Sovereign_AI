# Ollama Benchmark Summary — 22 June 2026

## Tests run
| Test | Model | Prompt | Result |
|------|-------|--------|--------|
| v1 Toets 1 | phi3:mini | AF — Forge doel | **2.4s** but **nonsense output** (hallucination) |
| v1 Toets 2 | phi3:mini | AF — Self-improvement | **>8 min**, stuck/garbage — killed |
| v2 Test A | phi3:mini | EN — one sentence | Wrong (guessed fiction) — ~80s total batch |
| v2 Test B | llama3.2 | EN — one sentence | Wrong (confused with China forge) |

## Root cause analysis

### 1. RAM pressure (PRIMARY)
```
Total RAM:  37 GB
Used:       33 GB
Free:       <600 MB
Available:  ~5.4 GB
Swap used:  841 MB
```
**Ollama models compete with Chrome, GNOME, Bluemail, etc.** With 32GB already used, model load + inference triggers swap → slow + degraded quality.

### 2. Model knowledge (EXPECTED)
phi3:mini and llama3.2 don't know "Sovereign Forge Engine" — it's your private project. Use **RAG/context injection** (GROK.md, plan.md in prompt) or **Gemini** for unstructured tasks.

### 3. Afrikaans on small models (QUALITY)
phi3:mini produces poor Afrikaans for technical topics. Prefer:
- **English prompts** for Ollama fast path
- **afrikaans-boffin** for AF copy (if RAM allows)
- **Gemini** for polished bilingual public copy

## Recommendations
1. **Before Ollama sessions:** Close Chrome tabs / Bluemail — target **>10 GB free RAM**
2. **Default fast model:** `llama3.2` (English) or `phi3:mini` with context in prompt
3. **Afrikaans:** `afrikaans-boffin` or Gemini — not phi3:mini alone
4. **Hybrid routing:** Ollama for private/quick + injected context; Gemini for LinkedIn/research
5. **Optional:** Unload unused models: `ollama stop gemma3n` (7.5GB) if not needed

## Log file
`progress/ollama_benchmark_20260622.log`