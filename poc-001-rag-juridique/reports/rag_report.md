# Rapport POC-001 - RAG juridique

Questions: 15
Retrieval accuracy: 86.67%
Grounded answers: 86.67%
Score RAGAS-like: 0.867

| Question | Top doc | Score | Hit | Grounded |
| --- | --- | ---: | --- | --- |
| Combien de temps dure l'obligation de confidentialite ? | doc-009 | 0.103 | False | False |
| Quelles informations RGPD doivent etre documentees ? | doc-006 | 0.129 | False | False |
| Un sous-traitant peut-il etre utilise librement ? | doc-003 | 0.490 | True | True |
| Quel delai pour remettre les elements de reversibilite ? | doc-004 | 0.129 | True | True |
| Quand les livrables sont-ils cedes au client ? | doc-005 | 0.488 | True | True |
| Quelles regles pour les acces administrateurs ? | doc-006 | 0.298 | True | True |
| Quel est le delai de prise en charge d'un incident critique ? | doc-007 | 0.080 | True | True |
| Quel preavis avant un audit de conformite ? | doc-008 | 0.471 | True | True |
| Comment est limitee la responsabilite du prestataire ? | doc-009 | 0.530 | True | True |
| Quand une partie peut-elle resilier ? | doc-010 | 0.378 | True | True |
| La MFA est-elle obligatoire ? | doc-006 | 0.183 | True | True |
| Les composants open source sont-ils cedes ? | doc-005 | 0.445 | True | True |
| Que contient un rapport apres incident ? | doc-007 | 0.175 | True | True |
| L'audit peut-il perturber l'exploitation ? | doc-008 | 0.408 | True | True |
| Quel document parle de format ouvert ? | doc-004 | 0.258 | True | True |

## Takeaways

- Recherche par frequence des termes sur la clause entiere : ni decoupage, ni modele vectoriel, ni generation de reponse.
- Les deux echecs portent sur des questions dont la reponse figure dans le corpus.
- Le jeu ne comporte aucune question hors corpus : la capacite a refuser n'est pas mesuree.
- Score composite maison (0,6 x recherche + 0,4 x presence des termes attendus), qui n'est pas une evaluation RAGAS.
