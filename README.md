# Oppdrag public POCs

[![validate-pocs](https://github.com/ForOppdrag/oppdrag-public-pocs/actions/workflows/validate.yml/badge.svg)](https://github.com/ForOppdrag/oppdrag-public-pocs/actions/workflows/validate.yml)

Mini proof-of-concepts publics qui accompagnent la page **Build in Public** d'Oppdrag.Tech.

Notre ligne : montrer l'exécution. Chaque POC part d'un besoin réaliste, utilise uniquement des données synthétiques, produit un résultat mesurable et documente aussi ses limites.

## Pourquoi ce dépôt existe

N'importe qui peut se dire expert IA, Data ou Cyber. Nous préférons publier des preuves : code lisible, rapports, hypothèses, métriques et takeaways honnêtes.

## POCs publiés

| ID | Domaine | POC | Résultat documenté | Lancer |
| --- | --- | --- | --- | --- |
| POC-001 | IA générative | RAG documentaire sur corpus juridique | Score RAGAS-like `0.867` | `python poc-001-rag-juridique/src/rag_demo.py` |
| POC-002 | IA agentique | Agent de qualification des briefs mission | Complétude après clarification `94%` | `python poc-002-agent-qualification-briefs/src/brief_agent.py` |
| POC-003 | Data engineering | Pipeline KPI temps réel mission | Latence P99 `790ms` | `python poc-003-pipeline-kpi-temps-reel/src/stream_kpis.py` |
| POC-004 | Cybersécurité | Audit cloud AWS fictif | `23` findings, dont `5` critiques | `python poc-004-audit-cloud-aws-fictif/src/audit_config.py` |

## Format

Chaque POC suit le même cadre :

- **J+1 - Cadrage** : périmètre, hypothèses, données de test, critères de succès.
- **J+3 - Prototype** : première version fonctionnelle, métriques intermédiaires, blocages.
- **J+5 - Démo documentée** : rapport, résultats, limites et prochaines décisions.

## Exécution locale

Prérequis : Python 3.11+.

```bash
python poc-001-rag-juridique/src/rag_demo.py
python poc-002-agent-qualification-briefs/src/brief_agent.py
python poc-003-pipeline-kpi-temps-reel/src/stream_kpis.py
python poc-004-audit-cloud-aws-fictif/src/audit_config.py
```

Les rapports sont générés dans chaque dossier `reports/`.

## Données et sécurité

- Données synthétiques uniquement.
- Aucun secret, token, identifiant cloud ou donnée client.
- Le POC cyber n'effectue aucun scan : il audite un fichier JSON fictif.

## Liens

- Site : https://oppdrag.tech
- Build in public : https://oppdrag.tech/build-in-public
- Assets de marque : https://github.com/ForOppdrag/oppdrag-brand-assets
- Contact : contact@oppdrag.tech

## Licence

MIT, sauf mention contraire.