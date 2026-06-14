# POC-004 - Audit de configuration cloud AWS fictif

Objectif : auditer une architecture AWS volontairement mal configuree a partir d'un fichier JSON synthetique. Le script identifie les risques, attribue une severite et propose une remediation.

## Lancer

```bash
python src/audit_config.py
```

## Securite

Aucun scan cloud, aucune connexion AWS. Tout est local et fictif.
