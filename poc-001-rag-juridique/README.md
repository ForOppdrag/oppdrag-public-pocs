# POC-001 - Recherche documentaire sur un corpus juridique synthétique

## Ce que fait le script

- **Corpus** : 10 clauses contractuelles synthétiques (`data/legal_corpus.json`), de 111 à 193 caractères chacune : confidentialité, données personnelles, sous-traitance, réversibilité, propriété intellectuelle, sécurité, engagement de service, audit, responsabilité, résiliation.
- **Questions** : 15 (`data/questions.json`), chacune rattachée à la clause qui y répond (`expected_doc`) et aux termes que la réponse doit contenir (`answer_contains`).
- **Recherche** : pour chaque question, similarité cosinus entre la fréquence de ses termes et celle de chaque clause entière, après retrait de quelques mots vides. Il n'y a **ni découpage**, **ni modèle de représentation vectorielle**, **ni génération de réponse**.
- **Évaluation** :
  - recherche réussie si la clause classée première est la clause attendue ;
  - « réponse fondée » si cette clause contient au moins la moitié des termes attendus ;
  - score composite : `0,6 × taux de recherche réussie + 0,4 × taux de réponses fondées`.

## Résultat (`reports/rag_report.md`)

- Bonne clause en tête pour 13 questions sur 15 (86,67 %).
- Score composite : 0,867. Il est inspiré de RAGAS, **mais ce n'est pas une évaluation RAGAS**.
- Les deux échecs portent sur des questions dont la réponse figure dans le corpus : la durée de l'obligation de confidentialité, et les informations à documenter au titre du RGPD.

## Limites

- Le jeu ne comporte aucune question hors corpus : la capacité à refuser n'est pas mesurée.
- Le corpus est minuscule et synthétique ; le résultat ne dit rien d'une chaîne de recherche documentaire en production.

## Lancer

```bash
python src/rag_demo.py
```
