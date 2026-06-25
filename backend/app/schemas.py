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
