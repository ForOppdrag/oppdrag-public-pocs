# POC-003 - Agrégation d'événements de mission

## Ce que fait le script

- **Données** : 12 événements synthétiques (`data/events.jsonl`), chacun porteur d'une mission, d'un type (progression, livraison, alerte), d'une valeur et d'une latence `latency_ms`.
- **Agrégation** : par mission, la progression maximale et le nombre de livraisons, d'alertes et d'événements.
- **Centiles** : P95 et P99 des latences.

Il n'y a **ni flux**, **ni fenêtrage**, **ni brique Kafka, Flink ou ClickHouse** : le script lit un fichier et agrège en mémoire, en Python standard.

## Résultat (`reports/kpi_report.md`)

- 12 événements traités.
- Centiles P95 de 780 ms et P99 de 790 ms. **Ces latences sont des valeurs écrites dans le fichier de données, et non des mesures** : les centiles décrivent les données d'entrée, pas un traitement.

## Lancer

```bash
python src/stream_kpis.py
```
