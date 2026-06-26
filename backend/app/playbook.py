from typing import Dict, List

from app.pattern_engine import analyze_patterns


def calculate_confidence(patterns: Dict) -> Dict:
    cases_count = patterns.get("cases_analyzed", 0)
    action_patterns = patterns.get("action_patterns", [])
    tag_patterns = patterns.get("tag_patterns", [])

    evidence_score = min(cases_count * 18, 45)
    action_score = min(len(action_patterns) * 8, 35)
    tag_score = min(len(tag_patterns) * 5, 20)

    confidence = evidence_score + action_score + tag_score

    return {
        "score": min(confidence, 95),
        "basis": {
            "cases_analyzed": cases_count,
            "action_patterns": len(action_patterns),
            "capability_patterns": len(tag_patterns),
        },
    }


def build_objective(question: str, patterns: Dict) -> str:
    if patterns.get("cases_analyzed", 0) == 0:
        return "Not enough prior evidence to generate a reliable operating objective."

    return (
        "Create a repeatable operating approach based on prior portfolio engagements, "
        "using evidence from similar company challenges, actions taken, and observed outcomes."
    )


def build_roadmap(patterns: Dict) -> List[Dict]:
    action_patterns = patterns.get("action_patterns", [])

    early_actions = []
    middle_actions = []
    scaling_actions = []

    for item in action_patterns:
        action = item.get("pattern", "")

        lowered = action.lower()

        if any(word in lowered for word in ["created", "defined", "evaluating", "identify", "inventory"]):
            early_actions.append(action)
        elif any(word in lowered for word in ["built", "standardized", "introduced", "deployed"]):
            middle_actions.append(action)
        else:
            scaling_actions.append(action)

    return [
        {
            "phase": "Phase 1: Establish Ownership",
            "goal": "Create clarity around who owns the initiative and what success means.",
            "actions": early_actions[:4] or [
                "Identify the operating bottleneck",
                "Assign a cross-functional owner",
                "Define success metrics",
            ],
        },
        {
            "phase": "Phase 2: Build Repeatable Infrastructure",
            "goal": "Move from isolated efforts to reusable standards and workflows.",
            "actions": middle_actions[:4] or [
                "Standardize tooling and documentation",
                "Create shared operating processes",
                "Pilot the highest-value workflow",
            ],
        },
        {
            "phase": "Phase 3: Scale What Works",
            "goal": "Expand only after the initial operating model has shown measurable value.",
            "actions": scaling_actions[:4] or [
                "Scale successful pilots",
                "Hire specialists after validating demand",
                "Track business outcomes over time",
            ],
        },
    ]


def build_risks(patterns: Dict) -> List[str]:
    tags = [item.get("tag", "") for item in patterns.get("tag_patterns", [])]

    risks = []

    if "AI Adoption" in tags:
        risks.extend(
            [
                "Fragmented AI ownership across product, engineering, and operations",
                "Duplicate tooling or vendor spend before standards are defined",
                "Hiring specialized AI roles before validating high-value use cases",
            ]
        )

    if "Executive Hiring" in tags:
        risks.extend(
            [
                "Hiring for a title instead of the actual operating bottleneck",
                "Keeping decision-making too centralized with founders or early leaders",
            ]
        )

    if "Support Automation" in tags:
        risks.extend(
            [
                "Deploying automation externally before internal agent-assist workflows are proven",
                "Automating from outdated or inconsistent knowledge sources",
            ]
        )

    if not risks:
        risks = [
            "Treating the issue as a one-off project instead of a repeatable operating system",
            "Scaling the solution before validating ownership, process, and measurable outcomes",
        ]

    return risks[:5]


def build_evidence(patterns: Dict) -> List[Dict]:
    evidence = []

    for case in patterns.get("relevant_cases", []):
        evidence.append(
            {
                "company": case.get("company"),
                "stage": case.get("stage"),
                "sector": case.get("sector"),
                "problem": case.get("problem"),
                "outcome": case.get("outcome"),
                "lesson": case.get("lesson"),
                "source_file": case.get("source_file"),
            }
        )

    return evidence


def generate_operating_playbook(question: str, top_k: int = 5) -> Dict:
    patterns = analyze_patterns(question, top_k)
    confidence = calculate_confidence(patterns)

    return {
        "question": question,
        "title": "Operating Playbook",
        "objective": build_objective(question, patterns),
        "confidence": confidence,
        "pattern_summary": patterns.get("pattern_summary"),
        "recommended_roadmap": build_roadmap(patterns),
        "key_risks": build_risks(patterns),
        "supporting_evidence": build_evidence(patterns),
        "patterns_used": {
            "action_patterns": patterns.get("action_patterns", []),
            "capability_patterns": patterns.get("tag_patterns", []),
        },
    }