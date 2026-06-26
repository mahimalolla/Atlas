import os
import json
from typing import List, Dict
from app.config import DOCS_PATH


def parse_case_document(text: str, filename: str) -> Dict:
    """
    Phase 2 structured extraction.

    For the MVP, sample docs follow a semi-structured format.
    This parser converts them into normalized business cases.

    Future version:
    Replace this deterministic parser with an LLM extractor that can handle
    messy meeting notes, memos, emails, and portfolio updates.
    """

    sections = {
        "company": "",
        "stage": "",
        "sector": "",
        "problem": "",
        "root_cause": "",
        "actions_taken": "",
        "outcome": "",
        "lesson": "",
    }

    current_key = None

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        lower = line.lower()

        if lower.startswith("company:"):
            sections["company"] = line.split(":", 1)[1].strip()
        elif lower.startswith("stage:"):
            sections["stage"] = line.split(":", 1)[1].strip()
        elif lower.startswith("sector:"):
            sections["sector"] = line.split(":", 1)[1].strip()
        elif lower.startswith("problem:"):
            current_key = "problem"
        elif lower.startswith("root cause:"):
            current_key = "root_cause"
        elif lower.startswith("actions taken:"):
            current_key = "actions_taken"
        elif lower.startswith("outcome:"):
            current_key = "outcome"
        elif lower.startswith("lesson:"):
            current_key = "lesson"
        elif current_key:
            sections[current_key] += line + " "

    sections["source_file"] = filename
    sections["tags"] = infer_tags(sections)

    return sections


def infer_tags(case: Dict) -> List[str]:
    text = " ".join(str(v).lower() for v in case.values())
    tags = []

    keyword_map = {
        "AI adoption": ["ai", "automation", "llm", "model"],
        "Executive hiring": ["vp", "executive", "hiring", "cto"],
        "Support automation": ["support", "tickets", "agent"],
        "GTM scaling": ["sales", "gtm", "pipeline", "revenue"],
        "MLOps": ["mlops", "deployment", "models", "monitoring"],
        "Operating model": ["ownership", "governance", "standards"],
        "Team scaling": ["headcount", "team", "managers"],
    }

    for tag, keywords in keyword_map.items():
        if any(keyword in text for keyword in keywords):
            tags.append(tag)

    return tags


def extract_all_cases() -> Dict:
    cases = []

    for filename in os.listdir(DOCS_PATH):
        if not filename.endswith(".txt"):
            continue

        path = os.path.join(DOCS_PATH, filename)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        case = parse_case_document(text, filename)
        cases.append(case)

    output_path = os.path.join("data", "processed_cases.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cases, f, indent=2)

    return {
        "status": "success",
        "cases_extracted": len(cases),
        "output_path": output_path,
        "cases": cases
    }