from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "briefs.json"
REPORT = ROOT / "reports" / "qualification_report.md"

FIELDS = {
    "role": ["engineer", "expert", "developpeur", "data", "ia", "securite", "full stack"],
    "stack": ["dbt", "snowflake", "rag", "aws", "iam", "s3", "next.js", "postgres", "crm"],
    "duration": ["mois", "semaines", "duree"],
    "location": ["paris", "remote", "site"],
    "budget": ["budget", "eur", "tj", "jour"],
    "constraints": ["rgpd", "urgent", "production", "contraintes"],
}

QUESTIONS = {
    "role": "Quel profil exact doit etre priorise pour cette mission ?",
    "stack": "Quelles technologies sont obligatoires et lesquelles sont negociables ?",
    "duration": "Quelle duree cible et quel rythme de mission faut-il prevoir ?",
    "location": "Quel mode de travail est attendu : remote, hybride ou sur site ?",
    "budget": "Quel budget ou TJM plafond est valide pour ce besoin ?",
    "constraints": "Quelles contraintes de securite, conformite ou delai sont bloquantes ?",
}


def has_signal(text: str, keywords: list[str]) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in keywords)


def extract_budget(text: str) -> str | None:
    match = re.search(r"(\d{3,4})\s*(?:eur|euro|€)", text, flags=re.I)
    return match.group(1) + " EUR/j" if match else None


def classify_domain(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ["rag", "ia", "agent"]):
        return "IA"
    if any(word in lowered for word in ["data", "pipeline", "dbt", "snowflake", "kpi"]):
        return "DATA"
    if any(word in lowered for word in ["securite", "aws", "iam", "audit"]):
        return "CYBER"
    return "APP"


def main() -> None:
    briefs = json.loads(DATA.read_text(encoding="utf-8"))
    rows = []
    completion_sum = 0

    for brief in briefs:
        text = brief["text"]
        present = {field: has_signal(text, keywords) for field, keywords in FIELDS.items()}
        missing = [field for field, ok in present.items() if not ok]
        completion = round((len(FIELDS) - len(missing)) / len(FIELDS), 2)
        completion_sum += completion
        rows.append({
            "id": brief["id"],
            "domain": classify_domain(text),
            "completion": completion,
            "budget": extract_budget(text) or "a clarifier",
            "missing": missing,
            "questions": [QUESTIONS[field] for field in missing[:3]],
        })

    average = completion_sum / len(briefs)
    REPORT.parent.mkdir(exist_ok=True)
    lines = ["# Rapport POC-002 - Agent qualification briefs", "", f"Briefs testes: {len(briefs)}", f"Completude moyenne: {average:.0%}", "", "| Brief | Domaine | Completude | Budget | Champs manquants |", "| --- | --- | ---: | --- | --- |"]
    for row in rows:
        lines.append(f"| {row['id']} | {row['domain']} | {row['completion']:.0%} | {row['budget']} | {', '.join(row['missing']) or 'aucun'} |")
    lines.append("\n## Questions de clarification generees\n")
    for row in rows:
        lines.append(f"### {row['id']}")
        for question in row["questions"] or ["Aucune question prioritaire."]:
            lines.append(f"- {question}")
    lines.extend(["", "## Takeaways", "", "- Un noeud d'incertitude evite de structurer trop vite un brief ambigu.", "- La detection des champs critiques suffit a accelerer le cadrage initial.", "- Les questions doivent etre limitees aux manques les plus bloquants."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"POC-002 OK - completion={average:.0%} - report={REPORT}")


if __name__ == "__main__":
    main()
