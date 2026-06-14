# POC-001 - RAG documentaire sur corpus juridique

Objectif : simuler un systeme RAG sur un corpus juridique synthetique, avec chunking, retrieval lexical/vectoriel simplifie et evaluation type RAGAS.

## Lancer

```bash
python src/rag_demo.py
```

## Resultats attendus

- 15 questions de test.
- Score global proche de 0.82+ sur ce corpus synthetique.
- Rapport genere dans `reports/rag_report.md`.

## Limites

Ce POC utilise un moteur local sans LLM externe. Il reproduit la logique d'evaluation et de retrieval sans pretendre remplacer une stack production.
