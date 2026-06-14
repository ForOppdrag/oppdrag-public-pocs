# POC-002 - Agent de qualification des briefs mission

Objectif : analyser des briefs entrants, detecter les champs manquants, generer des questions de clarification et produire un brief structure pret pour matching.

## Lancer

```bash
python src/brief_agent.py
```

## Sortie

Le script produit `reports/qualification_report.md` avec les champs completes, questions posees et score de completude.
