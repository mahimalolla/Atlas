from typing import List, Optional
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3)
    top_k: Optional[int] = Field(default=5, ge=1, le=10)


class SourceChunk(BaseModel):
    document: str
    chunk_id: str
    text: str
    score: Optional[float] = None


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[SourceChunk]


class IngestResponse(BaseModel):
    status: str
    processed_docs: List[str]
    chunks_added: int


class BusinessCase(BaseModel):
    company: str
    stage: str
    sector: str
    problem: str
    root_cause: str
    actions_taken: List[str]
    outcome: str
    lesson: str
    tags: List[str]
    source_file: str


class CaseExtractionResponse(BaseModel):
    status: str
    documents_processed: int
    cases_extracted: int
    avg_tags_per_case: float
    output_path: str
    cases: List[BusinessCase]

class PatternRequest(BaseModel):
    question: str = Field(..., min_length=3)
    top_k: Optional[int] = Field(default=5, ge=1, le=10)