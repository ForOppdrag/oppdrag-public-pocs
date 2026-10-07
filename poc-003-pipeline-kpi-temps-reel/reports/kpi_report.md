# Rapport POC-003 - Pipeline KPI temps reel

Evenements traites: 12
Latence P95 (valeurs du fichier de donnees, non mesurees): 780 ms
Latence P99 (valeurs du fichier de donnees, non mesurees): 790 ms

| Mission | Progression | Livraisons | Alertes | Evenements |
| --- | ---: | ---: | ---: | ---: |
| M-100 | 55% | 1 | 0 | 3 |
| M-101 | 20% | 0 | 2 | 3 |
| M-102 | 40% | 1 | 0 | 2 |
| M-103 | 70% | 1 | 0 | 2 |
| M-104 | 10% | 0 | 1 | 2 |

## Takeaways

- Agregation en memoire d'un fichier de 12 evenements, en Python standard : ni flux, ni fenetrage, ni Kafka, Flink ou ClickHouse.
- Les latences sont des valeurs du fichier de donnees : les centiles decrivent l'entree, pas un traitement.
