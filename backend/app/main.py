from fastapi import FastAPI, HTTPException
from app.playbook import generate_operating_playbook
from app.case_extraction import extract_all_cases
from app.ingest import ingest_documents
from app.retrieval import generate_answer, retrieve_context
from app.pattern_engine import analyze_patterns
from app.schemas import (
    CaseExtractionResponse,
    IngestResponse,
    QueryRequest,
    QueryResponse,
    PatternRequest,
    PlaybookRequest,
)

app = FastAPI(
    title="Atlas API",
    description="Institutional knowledge engine for portfolio-scale operating playbooks.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "Atlas",
        "tagline": "Institutional Knowledge for Portfolio Scale",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ingest", response_model=IngestResponse)
def ingest():
    try:
        return ingest_documents(reset=True)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    try:
        sources = retrieve_context(request.question, request.top_k or 5)
        answer = generate_answer(request.question, sources)
        return {"question": request.question, "answer": answer, "sources": sources}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

@app.post("/extract-cases", response_model=CaseExtractionResponse)
def extract_cases():
    return extract_all_cases()

@app.post("/patterns")
def patterns(request: PatternRequest):
    try:
        return analyze_patterns(request.question, request.top_k or 5)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    
@app.post("/playbook")
def playbook(request: PlaybookRequest):
    try:
        return generate_operating_playbook(request.question, request.top_k or 5)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc