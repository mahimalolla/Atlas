import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_PATH = os.getenv("CHROMA_PATH", "data/chroma")
DOCS_PATH = os.getenv("DOCS_PATH", "data/sample_docs")


def require_openai_key() -> str:
    """Return the OpenAI API key or raise a clear setup error."""
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_openai_api_key_here":
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Copy .env.example to .env and add your key."
        )
    return OPENAI_API_KEY
