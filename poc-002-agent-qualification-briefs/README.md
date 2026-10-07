# POC-002 - Qualification de briefs par mots-clés

## Ce que fait le script

- **Données** : 5 briefs synthétiques (`data/briefs.json`).
- **Rubriques** : rôle, technologies, durée, lieu, budget, contraintes. Le script en détecte la présence par **mots-clés**, sans agent ni modèle de langage.
- **Domaine** : déduit de mots-clés (IA, DATA, CYBER, APP).
- **Budget** : extrait par expression régulière lorsqu'un montant en euros est présent.
- **Questions** : jusqu'à trois questions de clarification par brief, choisies parmi des questions prédéfinies, pour les rubriques manquantes.

## Résultat (`reports/qualification_report.md`)

- **Complétude initiale** : part des six rubriques détectées. Elle vaut 63 % en moyenne.
- **Complétude « après clarification »** : c'est une **valeur simulée**. Le script ajoute 15,5 points par question posée (trois au plus), comme si chaque question recevait une réponse. **Aucune clarification n'a lieu** ; les 94 % affichés ne sont pas une mesure.

## Limites connues

- La détection par sous-chaînes est fragile. Le mot-clé « ia » se retrouve dans d'autres mots (« industrialiser », « IAM »), si bien que les briefs 001 et 003, qui portent sur la donnée et sur la sécurité, sont classés « IA ».
- Une rubrique est jugée présente dès qu'un mot-clé apparaît, sans que sa valeur soit extraite ou vérifiée.

## Lancer

```bash
python src/brief_agent.py
```
