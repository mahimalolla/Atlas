import json
import os
from collections import Counter
from typing import Dict, List


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CASES_PATH = os.path.join(BASE_DIR, "data", "cases", "cases.json")


def load_cases() -> List[Dict]:
    if not os.path.exists(CASES_PATH):
        raise FileNotFoundError(
            "No extracted cases found. Run POST /extract-cases first."
        )

    with open(CASES_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def score_case(question: str, case: Dict) -> int:
    question_terms = set(question.lower().split())

    case_text = " ".join(
        [
            case.get("company", ""),
            case.get("stage", ""),
            case.get("sector", ""),
            case.get("problem", ""),
            case.get("root_cause", ""),
            " ".join(case.get("actions_taken", [])),
            case.get("outcome", ""),
            case.get("lesson", ""),
            " ".join(case.get("tags", [])),
        ]
    ).lower()

    score = 0

    for term in question_terms:
        if len(term) > 3 and term in case_text:
            score += 1

    return score


def find_relevant_cases(question: str, top_k: int = 5) -> List[Dict]:
    cases = load_cases()

    scored_cases = []

    for case in cases:
        score = score_case(question, case)

        if score > 0:
            case_with_score = dict(case)
            case_with_score["relevance_score"] = score
            scored_cases.append(case_with_score)

    scored_cases.sort(key=lambda item: item["relevance_score"], reverse=True)

    return scored_cases[:top_k]


def extract_action_patterns(cases: List[Dict]) -> List[Dict]:
    action_counter = Counter()

    for case in cases:
        for action in case.get("actions_taken", []):
            normalized = action.strip()

            if normalized:
                action_counter[normalized] += 1

    patterns = []

    for action, count in action_counter.most_common():
        patterns.append(
            {
                "pattern": action,
                "frequency": count,
                "supporting_companies": [
                    case.get("company")
                    for case in cases
                    if action in case.get("actions_taken", [])
                ],
            }
        )

    return patterns


def extract_tag_patterns(cases: List[Dict]) -> List[Dict]:
    tag_counter = Counter()

    for case in cases:
        for tag in case.get("tags", []):
            tag_counter[tag] += 1

    return [
        {
            "tag": tag,
            "frequency": count,
            "companies": [
                case.get("company")
                for case in cases
                if tag in case.get("tags", [])
            ],
        }
        for tag, count in tag_counter.most_common()
    ]


def extract_lessons(cases: List[Dict]) -> List[Dict]:
    return [
        {
            "company": case.get("company"),
            "lesson": case.get("lesson"),
            "outcome": case.get("outcome"),
        }
        for case in cases
    ]


def generate_pattern_summary(question: str, cases: List[Dict]) -> str:
    if not cases:
        return "No relevant prior cases were found."

    top_tags = extract_tag_patterns(cases)[:3]
    tag_names = [tag["tag"] for tag in top_tags]

    companies = [case.get("company") for case in cases]

    return (
        f"Atlas found {len(cases)} relevant operating cases across "
        f"{', '.join(companies)}. The strongest recurring themes were "
        f"{', '.join(tag_names) if tag_names else 'not enough signal yet'}. "
        "These cases suggest that successful interventions depend on clear ownership, "
        "sequenced execution, and reusable operating standards rather than one-off fixes."
    )


def analyze_patterns(question: str, top_k: int = 5) -> Dict:
    relevant_cases = find_relevant_cases(question, top_k)

    return {
        "question": question,
        "cases_analyzed": len(relevant_cases),
        "pattern_summary": generate_pattern_summary(question, relevant_cases),
        "relevant_cases": relevant_cases,
        "action_patterns": extract_action_patterns(relevant_cases),
        "tag_patterns": extract_tag_patterns(relevant_cases),
        "lessons": extract_lessons(relevant_cases),
    }