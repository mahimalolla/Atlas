import os
import json
from typing import Dict, List

from app.config import DOCS_PATH


OUTPUT_DIR = os.path.join("data", "cases")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "cases.json")


def split_actions(actions_text: str) -> List[str]:
    actions = []

    for sentence in actions_text.split("."):
        cleaned = sentence.strip()

        if cleaned:
            actions.append(cleaned)

    return actions


def infer_tags(case: Dict) -> List[str]:
    text = " ".join(str(value).lower() for value in case.values())

    keyword_map = {
        "AI Adoption": ["ai", "automation", "llm", "model", "assistant"],
        "Executive Hiring": ["vp", "executive", "hiring", "cto"],
        "Support Automation": ["support", "tickets", "agent", "help center"],
        "GTM Scaling": ["sales", "gtm", "pipeline", "revenue"],
        "MLOps": ["mlops", "deployment", "monitoring", "inference"],
        "Operating Model": ["ownership", "governance", "standards"],
        "Team Scaling": ["headcount", "team", "managers"],
        "Knowledge Management": ["documentation", "knowledge base", "notes"],
    }

    tags = []

    for tag, keywords in keyword_map.items():
        if any(keyword in text for keyword in keywords):
            tags.append(tag)

    return tags


def parse_case_document(text: str, filename: str) -> Dict:
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
            current_key = None
        elif lower.startswith("stage:"):
            sections["stage"] = line.split(":", 1)[1].strip()
            current_key = None
        elif lower.startswith("sector:"):
            sections["sector"] = line.split(":", 1)[1].strip()
            current_key = None
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

    case = {
        "company": sections["company"],
        "stage": sections["stage"],
        "sector": sections["sector"],
        "problem": sections["problem"].strip(),
        "root_cause": sections["root_cause"].strip(),
        "actions_taken": split_actions(sections["actions_taken"]),
        "outcome": sections["outcome"].strip(),
        "lesson": sections["lesson"].strip(),
        "tags": [],
        "source_file": filename,
    }

    case["tags"] = infer_tags(case)

    return case


def extract_all_cases() -> Dict:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cases = []

    for filename in os.listdir(DOCS_PATH):
        if not filename.endswith(".txt"):
            continue

        path = os.path.join(DOCS_PATH, filename)

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        cases.append(parse_case_document(text, filename))

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        json.dump(cases, file, indent=2)

    total_tags = sum(len(case["tags"]) for case in cases)
    avg_tags = round(total_tags / len(cases), 2) if cases else 0

    return {
        "status": "success",
        "documents_processed": len(cases),
        "cases_extracted": len(cases),
        "avg_tags_per_case": avg_tags,
        "output_path": OUTPUT_PATH,
        "cases": cases,
    }