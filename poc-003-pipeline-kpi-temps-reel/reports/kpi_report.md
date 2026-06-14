# Rapport POC-003 - Pipeline KPI temps reel

Evenements traites: 12
Latence P95: 780 ms
Latence P99: 790 ms

| Mission | Progression | Livraisons | Alertes | Evenements |
| --- | ---: | ---: | ---: | ---: |
| M-100 | 55% | 1 | 0 | 3 |
| M-101 | 20% | 0 | 2 | 3 |
| M-102 | 40% | 1 | 0 | 2 |
| M-103 | 70% | 1 | 0 | 2 |
| M-104 | 10% | 0 | 1 | 2 |

## Takeaways

- Le schema d'evenement doit etre stable avant de brancher le dashboard.
- La latence P99 est plus utile que la moyenne pour piloter les alertes.
- Une base analytique type ClickHouse convient mieux aux agregats rapides qu'une base transactionnelle seule.
