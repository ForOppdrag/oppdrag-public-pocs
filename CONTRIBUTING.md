# Contribuer

Les POCs doivent rester simples, reproductibles et sans donnees sensibles.

Avant une PR :

```bash
python poc-001-rag-juridique/src/rag_demo.py
python poc-003-pipeline-kpi-temps-reel/src/stream_kpis.py
python poc-004-audit-cloud-aws-fictif/src/audit_config.py
```

Merci d'ajouter un court rapport dans `reports/` pour toute evolution significative.

## Décrire ce que fait le code

- Le README de chaque POC décrit ce que fait réellement le script : méthode, données, résultat du rapport, limites.
- Toute métrique citée renvoie au rapport généré. Une valeur simulée ou fournie par les données d'entrée est désignée comme telle.
- Aucune technologie n'est citée si le code ne l'emploie pas.
