# CyHelm Control Atlas

An UAE-first compliance mapping demonstrator with searchable, versioned crosswalks, explicit mapping strength, review status, rationale, and JSON export.

## Run

```powershell
npm start
```

Open `http://127.0.0.1:4173`. No installation or AI key is required.

## Optional AI

The mapping critic uses any OpenAI-compatible endpoint. Keys stay in the server process.

```powershell
$env:CYHELM_AI_BASE_URL='http://127.0.0.1:11434/v1'
$env:CYHELM_AI_MODEL='qwen3:8b'
npm start
```

For hosted providers, set `CYHELM_AI_API_KEY` as well. Do not commit secrets.

## Data notice

The included records are illustrative CyHelm-authored summaries. They do not reproduce an official standard and are not a substitute for licensed source documents or professional interpretation.

