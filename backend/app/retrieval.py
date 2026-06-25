from typing import Dict, List

import chromadb
from openai import OpenAI

from app.config import CHROMA_PATH, require_openai_key
from app.ingest import COLLECTION_NAME, EMBEDDING_MODEL

CHAT_MODEL = "gpt-4o-mini"


def get_collection():
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    return chroma_client.get_or_create_collection(name=COLLECTION_NAME)


def embed_query(question: str) -> List[float]:
    client = OpenAI(api_key=require_openai_key())
    response = client.embeddings.create(model=EMBEDDING_MODEL, input=[question])
    return response.data[0].embedding


def retrieve_context(question: str, top_k: int = 5) -> List[Dict]:
    collection = get_collection()
    query_embedding = embed_query(question)

    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)

    sources: List[Dict] = []
    docs = results.get("documents", [[]])[0]
    ids = results.get("ids", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for idx, doc in enumerate(docs):
        metadata = metadatas[idx] if idx < len(metadatas) else {}
        distance = distances[idx] if idx < len(distances) else None
        sources.append(
            {
                "document": metadata.get("document", "unknown"),
                "chunk_id": ids[idx],
                "text": doc,
                "score": distance,
            }
        )

    return sources


def generate_answer(question: str, sources: List[Dict]) -> str:
    client = OpenAI(api_key=require_openai_key())

    context = "\n\n".join(
        f"SOURCE: {source['document']}\n{source['text']}" for source in sources
    )

    prompt = f"""
You are Atlas, an AI operating intelligence system for growth equity teams.

Your job is to convert scattered portfolio knowledge into reusable operating guidance.
Use only the context below. Do not invent company facts that are not in the context.

Return the answer in this exact structure:

## Direct Answer
A concise recommendation.

## Similar Past Cases
Bullet list of relevant companies and what happened.

## Recurring Pattern
The cross-case insight that transfers across companies.

## Recommended Playbook
Numbered steps that an operating team could reuse.

## Evidence Used
Mention the source documents you relied on.

QUESTION:
{question}

CONTEXT:
{context}
"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are precise, practical, and business-oriented. You explain AI systems as reusable operating leverage, not as generic chatbots.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.25,
    )

    return response.choices[0].message.content or "No answer generated."
