# Atlas

**Institutional Knowledge for Portfolio Scale**

Atlas helps investment and operating teams transform repeated portfolio challenges into reusable AI-generated playbooks.

## Product Thesis

Inside a growth equity firm, one of the highest-leverage assets is not just capital. It is accumulated operating knowledge: the lessons, patterns, and interventions learned from helping many companies scale.

But that knowledge often lives across meeting notes, investment memos, Slack threads, advisor calls, and individual partner experience.

Atlas turns those scattered records into structured, reusable guidance.

## MVP Demo

A portfolio CEO asks:

> How should a Series B SaaS company build its first AI team?

Atlas retrieves similar past cases, identifies recurring patterns, and generates a practical playbook that an operating team could reuse.

## Current Scope

This repository currently includes the Phase 1 backend:

- FastAPI API
- Chroma vector store
- OpenAI embeddings
- Sample synthetic portfolio case docs
- Retrieval-augmented answer generation

## Roadmap

### Phase 1
Working backend with ingestion, retrieval, and structured answers.

### Phase 2
Case extraction and pattern mining:

- Company
- Stage
- Problem
- Root cause
- Actions taken
- Outcome
- Lessons learned

### Phase 3
Frontend demo and playbook export.

## Run Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```
