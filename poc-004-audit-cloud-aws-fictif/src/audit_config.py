from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "data" / "aws_reference_architecture.json"
REPORT = ROOT / "reports" / "audit_report.md"


def finding(fid: str, severity: str, asset: str, issue: str, remediation: str) -> dict[str, str]:
    return {"id": fid, "severity": severity, "asset": asset, "issue": issue, "remediation": remediation}


def main() -> None:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    findings: list[dict[str, str]] = []

    for user in cfg["iam_users"]:
        if user["policy"] == "AdministratorAccess" and not user["mfa"]:
            findings.append(finding("IAM-001", "CRITICAL", user["name"], "Compte administrateur sans MFA.", "Activer MFA et remplacer le compte partage par des roles nominatifs."))
        if user["last_rotated_days"] > 180:
            findings.append(finding("IAM-002", "HIGH", user["name"], "Cle ou secret non tourne depuis plus de 180 jours.", "Mettre en place une rotation automatique et supprimer les cles dormantes."))

    for bucket in cfg["s3_buckets"]:
        if bucket["public"]:
            findings.append(finding("S3-001", "HIGH", bucket["name"], "Bucket public detecte.", "Activer Block Public Access et limiter les policies au besoin exact."))
        if not bucket["encryption"]:
            findings.append(finding("S3-002", "MEDIUM", bucket["name"], "Chiffrement au repos desactive.", "Activer SSE-S3 ou SSE-KMS."))
        if not bucket["versioning"]:
            findings.append(finding("S3-003", "LOW", bucket["name"], "Versioning desactive.", "Activer le versioning pour faciliter restauration et forensic."))

    for sg in cfg["security_groups"]:
        if sg["port"] == 22 and sg["cidr"] == "0.0.0.0/0":
            findings.append(finding("NET-001", "CRITICAL", sg["name"], "SSH expose a Internet.", "Restreindre a un bastion, VPN ou SSM Session Manager."))
        if sg["port"] in (5432, 3306, 6379) and sg["cidr"] == "0.0.0.0/0":
            findings.append(finding("NET-002", "CRITICAL", sg["name"], "Base de donnees exposee publiquement.", "Limiter aux subnets applicatifs prives."))

    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    findings.sort(key=lambda item: severity_order[item["severity"]])
    counts = {sev: sum(1 for f in findings if f["severity"] == sev) for sev in severity_order}

    REPORT.parent.mkdir(exist_ok=True)
    lines = ["# Rapport POC-004 - Audit cloud AWS fictif", "", f"Findings: {len(findings)}", f"Critiques: {counts['CRITICAL']}", f"High: {counts['HIGH']}", f"Medium: {counts['MEDIUM']}", f"Low: {counts['LOW']}", "", "| ID | Severite | Actif | Probleme | Remediation |", "| --- | --- | --- | --- | --- |"]
    for f in findings:
        lines.append(f"| {f['id']} | {f['severity']} | {f['asset']} | {f['issue']} | {f['remediation']} |")
    lines.extend(["", "## Takeaways", "", "- Les risques IAM et exposition reseau dominent les findings critiques.", "- Un scoring contextualise rend la priorisation plus actionnable.", "- Le rapport doit inclure la validation des corrections, pas seulement la detection."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"POC-004 OK - findings={len(findings)} critical={counts['CRITICAL']} - report={REPORT}")


if __name__ == "__main__":
    main()
