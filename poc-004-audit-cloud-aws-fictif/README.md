# POC-004 - Audit de configuration cloud AWS fictif

## Ce que fait le script

- **Données** : la description JSON d'une architecture AWS fictive, volontairement mal configurée (`data/aws_reference_architecture.json`) : utilisateurs IAM, buckets S3, groupes de sécurité.
- **Contrôles** : sept règles, chacune avec une **sévérité fixe** et une remédiation :
  - administrateur sans MFA (critique) ;
  - clé non tournée depuis plus de 180 jours (élevée) ;
  - bucket public (élevée) ;
  - chiffrement au repos désactivé (moyenne) ;
  - versioning désactivé (faible) ;
  - SSH ouvert à internet (critique) ;
  - base de données ouverte à internet (critique).

## Résultat (`reports/audit_report.md`)

- 23 constats, dont 5 critiques, 6 élevés, 6 moyens et 6 faibles, classés par sévérité.
- Une remédiation est proposée pour chaque constat. **Aucune correction n'est appliquée ni vérifiée.**

## Sécurité

Aucun scan cloud, aucune connexion AWS. Tout est local et fictif.

## Lancer

```bash
python src/audit_config.py
```
