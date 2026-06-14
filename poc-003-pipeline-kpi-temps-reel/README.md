# POC-003 - Pipeline data temps reel KPI mission

Objectif : simuler un pipeline streaming Kafka -> Flink -> ClickHouse avec Python standard library : ingestion d'evenements, fenetrage, agregats et controle de latence.

## Lancer

```bash
python src/stream_kpis.py
```

## Sortie

Le rapport `reports/kpi_report.md` resume les volumes, latences et KPIs par mission.
