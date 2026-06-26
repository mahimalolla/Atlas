import json
import os
from collections import Counter
from typing import Dict, List

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CASES_PATH = os.path.join(BASE_DIR, "data", "cases", "cases.json")


def load_cases() -> List[Dict]:
    if not os.path.exists(CASES_PATH):
        raise FileNotFoundError(
            "No extracted cases found. Run /extract-cases first."
        )

    with open(CASES_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def top_capabilities(cases: List[Dict]) -> List[Dict]:
    counter = Counter()

    for case in cases:
        for tag in case.get("tags", []):
            counter[tag] += 1

    return [
        {
            "capability": capability,
            "count": count
        }
        for capability, count in counter.most_common()
    ]


def recurring_bottlenecks(cases: List[Dict]) -> List[Dict]:
    keywords = Counter()

    important_words = [
        "ownership",
        "governance",
        "documentation",
        "hiring",
        "support",
        "automation",
        "scaling",
        "coordination",
        "knowledge",
        "vendors"
    ]

    for case in cases:
        text = (
            case.get("problem", "") +
            " " +
            case.get("root_cause", "")
        ).lower()

        for word in important_words:
            if word in text:
                keywords[word] += 1

    return [
        {
            "bottleneck": word,
            "frequency": count
        }
        for word, count in keywords.most_common()
    ]


def successful_interventions(cases: List[Dict]) -> List[Dict]:
    actions = Counter()

    for case in cases:
        for action in case.get("actions_taken", []):
            actions[action.strip()] += 1

    return [
        {
            "intervention": action,
            "frequency": count
        }
        for action, count in actions.most_common()
    ]


def portfolio_score(cases: List[Dict]) -> Dict:
    total_cases = len(cases)

    capabilities = len(top_capabilities(cases))

    score = min(
        100,
        45 +
        capabilities * 5 +
        total_cases * 3
    )

    return {
        "score": score,
        "confidence": "High" if score >= 80 else "Medium"
    }


def emerging_opportunities(cases: List[Dict]) -> List[str]:

    opportunities = []

    capabilities = [c["capability"] for c in top_capabilities(cases)]

    if "AI Adoption" in capabilities:
        opportunities.append(
            "Standardize AI governance across portfolio companies."
        )

    if "Support Automation" in capabilities:
        opportunities.append(
            "Deploy internal AI assistants before customer-facing automation."
        )

    if "Executive Hiring" in capabilities:
        opportunities.append(
            "Create repeatable executive hiring playbooks."
        )

    opportunities.append(
        "Capture institutional knowledge as reusable operating frameworks."
    )

    return opportunities


def atlas_intelligence() -> Dict:

    cases = load_cases()

    return {
        "portfolio_summary": {
            "engagements": len(cases),
            "companies": len(
                set(case["company"] for case in cases)
            ),
            "capabilities": len(top_capabilities(cases))
        },

        "portfolio_health": portfolio_score(cases),

        "top_capabilities": top_capabilities(cases),

        "recurring_bottlenecks": recurring_bottlenecks(cases),

        "successful_interventions": successful_interventions(cases),

        "emerging_opportunities": emerging_opportunities(cases)
    }