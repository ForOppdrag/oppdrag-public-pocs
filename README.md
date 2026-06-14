# Oppdrag public POCs

Mini proof-of-concepts publics qui accompagnent la page **Build in Public** d'Oppdrag.

Ces POCs sont volontairement reproductibles en local, sans donnees client et sans dependances cloud. Ils servent a montrer la methode : cadrage, prototype, demo documentee, resultats et limites.

## POCs

| ID | Domaine | POC | Execution rapide |
| --- | --- | --- | --- |
| POC-001 | IA generative | RAG documentaire sur corpus juridique | `python poc-001-rag-juridique/src/rag_demo.py` |
| POC-002 | IA agentique | Agent de qualification des briefs mission | `python poc-002-agent-qualification-briefs/src/brief_agent.py` |
| POC-003 | Data engineering | Pipeline KPI temps reel mission | `python poc-003-pipeline-kpi-temps-reel/src/stream_kpis.py` |
| POC-004 | Cybersecurite | Audit cloud AWS fictif | `python poc-004-audit-cloud-aws-fictif/src/audit_config.py` |

## Prerequis

- Python 3.11+
- Aucune dependance externe obligatoire

## Lancer toutes les demos

```bash
python poc-001-rag-juridique/src/rag_demo.py
python poc-002-agent-qualification-briefs/src/brief_agent.py
python poc-003-pipeline-kpi-temps-reel/src/stream_kpis.py
python poc-004-audit-cloud-aws-fictif/src/audit_config.py
```

## Ethique et donnees

- Donnees synthetiques uniquement.
- Pas de secret, pas d'identifiant cloud reel, pas de donnee client.
- Le POC cyber est un audit statique de fichiers fictifs, sans scan d'infrastructure.

## Licence

MIT, sauf mention contraire.
