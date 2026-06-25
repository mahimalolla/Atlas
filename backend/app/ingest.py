import os
import uuid
from typing import Dict, List

import chromadb
from openai import OpenAI

from app.config import CHROMA_PATH, DOCS_PATH, require_openai_key

COLLECTION_NAME = "atlas_knowledge"
EMBEDDING_MODEL = "text-embedding-3-small"


def chunk_text(text: str, chunk_size: int = 950, overlap: int = 175) -> List[str]:
    """Simple character chunker. Good enough for MVP and transparent for reviewers."""
    clean = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    chunks = []
    start = 0

    while start < len(clean):
        end = start + chunk_size
        chunks.append(clean[start:end])
        start += chunk_size - overlap

    return chunks


def get_collection():
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    return chroma_client.get_or_create_collection(name=COLLECTION_NAME)


def embed_texts(texts: List[str]) -> List[List[float]]:
    client = OpenAI(api_key=require_openai_key())
    response = client.embeddings.create(model=EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]


def ingest_documents(reset: bool = True) -> Dict:
    """Ingest all .txt files into Chroma. Reset by default for deterministic demos."""
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

    if reset:
        try:
            chroma_client.delete_collection(name=COLLECTION_NAME)
        except Exception:
            pass

    collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)

    added_chunks = 0
    processed_docs: List[str] = []

    if not os.path.isdir(DOCS_PATH):
        raise FileNotFoundError(f"Docs path not found: {DOCS_PATH}")

    for filename in sorted(os.listdir(DOCS_PATH)):
        if not filename.endswith(".txt"):
            continue

        path = os.path.join(DOCS_PATH, filename)
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        chunks = chunk_text(text)
        if not chunks:
            continue

        embeddings = embed_texts(chunks)
        ids = []
        metadatas = []

        for idx, _chunk in enumerate(chunks):
            ids.append(f"{filename}-{idx}-{uuid.uuid4().hex[:8]}")
            metadatas.append({"document": filename, "chunk_index": idx})

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        processed_docs.append(filename)
        added_chunks += len(chunks)

    return {
        "status": "success",
        "processed_docs": processed_docs,
        "chunks_added": added_chunks,
    }
