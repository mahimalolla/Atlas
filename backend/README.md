# Atlas Backend

Atlas is an institutional knowledge engine for growth equity and operating teams.

It turns scattered portfolio knowledge into reusable AI-generated operating playbooks.

## Why Atlas

Investment and operating teams often solve similar portfolio problems repeatedly:

- How should a company build its first AI team?
- When should a founder hire a VP Engineering?
- Should support automation start internally or customer-facing?
- How do you turn founder-led sales into a repeatable GTM motion?

The knowledge exists, but it is trapped in meeting notes, memos, Slack threads, and individual experience.

Atlas retrieves similar past cases, identifies recurring patterns, and generates reusable playbooks.

## Phase 1 Features

- Ingest `.txt` portfolio case notes
- Chunk and embed documents with OpenAI embeddings
- Store embeddings in Chroma
- Retrieve relevant case evidence
- Generate structured answers with similar cases, recurring patterns, and a reusable playbook

## Tech Stack

- FastAPI
- ChromaDB
- OpenAI embeddings and chat completions
- Python

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add your OpenAI API key to `.env`.

## Run

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Demo Flow

1. Call `POST /ingest`
2. Call `POST /query`

Example query:

```json
{
  "question": "How should a Series B SaaS company build its first AI team?",
  "top_k": 5
}
```

Expected output sections:

- Direct Answer
- Similar Past Cases
- Recurring Pattern
- Recommended Playbook
- Evidence Used

## Project Positioning

Atlas is not a generic chatbot. It is a pattern-mining and playbook-generation layer for portfolio operations.

The goal is to help an investment firm reuse operating knowledge across many companies instead of solving the same problem from scratch every time.
