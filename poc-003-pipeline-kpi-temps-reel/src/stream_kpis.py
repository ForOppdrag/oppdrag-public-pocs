from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / "data" / "events.jsonl"
REPORT = ROOT / "reports" / "kpi_report.md"


def percentile(values: list[int], p: float) -> int:
    if not values:
        return 0
    values = sorted(values)
    index = min(len(values) - 1, round((len(values) - 1) * p))
    return values[index]


def main() -> None:
    aggregates = defaultdict(lambda: {"progress": 0, "deliveries": 0, "alerts": 0, "events": 0})
    latencies: list[int] = []

    for line in EVENTS.read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        mission = aggregates[event["mission_id"]]
        mission["events"] += 1
        latencies.append(event["latency_ms"])
        if event["type"] == "progress":
            mission["progress"] = max(mission["progress"], event["value"])
        elif event["type"] == "delivery":
            mission["deliveries"] += event["value"]
        elif event["type"] == "alert":
            mission["alerts"] += event["value"]

    p99 = percentile(latencies, 0.99)
    p95 = percentile(latencies, 0.95)
    REPORT.parent.mkdir(exist_ok=True)
    lines = ["# Rapport POC-003 - Pipeline KPI temps reel", "", f"Evenements traites: {len(latencies)}", f"Latence P95: {p95} ms", f"Latence P99: {p99} ms", "", "| Mission | Progression | Livraisons | Alertes | Evenements |", "| --- | ---: | ---: | ---: | ---: |"]
    for mission_id, agg in sorted(aggregates.items()):
        lines.append(f"| {mission_id} | {agg['progress']}% | {agg['deliveries']} | {agg['alerts']} | {agg['events']} |")
    lines.extend(["", "## Takeaways", "", "- Le schema d'evenement doit etre stable avant de brancher le dashboard.", "- La latence P99 est plus utile que la moyenne pour piloter les alertes.", "- Une base analytique type ClickHouse convient mieux aux agregats rapides qu'une base transactionnelle seule."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"POC-003 OK - p99={p99}ms - report={REPORT}")


if __name__ == "__main__":
    main()
