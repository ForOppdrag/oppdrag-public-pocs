# Oppdrag public POCs

[![validate-pocs](https://github.com/ForOppdrag/oppdrag-public-pocs/actions/workflows/validate.yml/badge.svg)](https://github.com/ForOppdrag/oppdrag-public-pocs/actions/workflows/validate.yml)

Maquettes publiques, volontairement simples, qui accompagnent la page **Build in Public** d'Oppdrag.Tech.

Chaque POC est un script en Python standard (aucune dépendance), appliqué à des données synthétiques, qui génère son propre rapport. Ce sont des illustrations de méthode à petite échelle : aucun ne reproduit une chaîne de production, et ce README décrit exactement ce que fait chaque script, limites comprises.

## POCs publiés

| ID | Domaine | Ce que fait le script | Résultat du rapport | Lancer |
| --- | --- | --- | --- | --- |
| POC-001 | Recherche documentaire | Classe 10 clauses contractuelles synthétiques par similarité de fréquence des termes avec chaque question ; aucun découpage, aucun modèle vectoriel, aucune génération de réponse. | Bonne clause en tête pour 13 questions sur 15 ; score composite maison `0.867` (0,6 × recherche + 0,4 × présence des termes attendus), qui n'est pas une évaluation RAGAS. | `python poc-001-rag-juridique/src/rag_demo.py` |
| POC-002 | Qualification de briefs | Repère par mots-clés six rubriques dans 5 briefs synthétiques et propose jusqu'à trois questions par brief ; aucun agent, aucun modèle de langage. | Complétude initiale moyenne `63%`. La valeur « après clarification » (`94%`) est **simulée** : aucune réponse n'est obtenue (voir le README du POC). | `python poc-002-agent-qualification-briefs/src/brief_agent.py` |
| POC-003 | Agrégation d'événements | Agrège 12 événements synthétiques par mission et calcule des centiles de latence ; aucune brique Kafka, Flink ou ClickHouse. | Centiles `P95 780ms` et `P99 790ms` calculés sur des latences **écrites dans le fichier de données**, et non mesurées. | `python poc-003-pipeline-kpi-temps-reel/src/stream_kpis.py` |
| POC-004 | Cybersécurité | Applique sept règles de contrôle à la description JSON d'une architecture AWS fictive ; aucune connexion à AWS. | `23` constats, dont `5` critiques, avec une remédiation proposée pour chacun ; aucune correction appliquée. | `python poc-004-audit-cloud-aws-fictif/src/audit_config.py` |

## Contenu de chaque dossier

- `src/` : le script ;
- `data/` : les données synthétiques ;
- `reports/` : le rapport généré par le script, reproductible à l'identique.

## Exécution locale

Prérequis : Python 3.11+.

```bash
python poc-001-rag-juridique/src/rag_demo.py
python poc-002-agent-qualification-briefs/src/brief_agent.py
python poc-003-pipeline-kpi-temps-reel/src/stream_kpis.py
python poc-004-audit-cloud-aws-fictif/src/audit_config.py
```

Les rapports sont régénérés dans chaque dossier `reports/`.

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
