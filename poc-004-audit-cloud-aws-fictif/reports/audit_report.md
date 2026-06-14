# Rapport POC-004 - Audit cloud AWS fictif

Findings: 23
Critiques: 5
High: 6
Medium: 6
Low: 6

| ID | Severite | Actif | Probleme | Remediation |
| --- | --- | --- | --- | --- |
| IAM-001 | CRITICAL | admin-shared | Compte administrateur sans MFA. | Activer MFA et remplacer le compte partage par des roles nominatifs. |
| IAM-001 | CRITICAL | root-breakglass | Compte administrateur sans MFA. | Activer MFA et remplacer le compte partage par des roles nominatifs. |
| IAM-001 | CRITICAL | legacy-ops-admin | Compte administrateur sans MFA. | Activer MFA et remplacer le compte partage par des roles nominatifs. |
| NET-001 | CRITICAL | ssh-admin | SSH expose a Internet. | Restreindre a un bastion, VPN ou SSM Session Manager. |
| NET-002 | CRITICAL | postgres-public | Base de donnees exposee publiquement. | Limiter aux subnets applicatifs prives. |
| IAM-002 | HIGH | admin-shared | Cle ou secret non tourne depuis plus de 180 jours. | Mettre en place une rotation automatique et supprimer les cles dormantes. |
| IAM-002 | HIGH | root-breakglass | Cle ou secret non tourne depuis plus de 180 jours. | Mettre en place une rotation automatique et supprimer les cles dormantes. |
| IAM-002 | HIGH | legacy-ops-admin | Cle ou secret non tourne depuis plus de 180 jours. | Mettre en place une rotation automatique et supprimer les cles dormantes. |
| IAM-002 | HIGH | readonly-audit | Cle ou secret non tourne depuis plus de 180 jours. | Mettre en place une rotation automatique et supprimer les cles dormantes. |
| S3-001 | HIGH | oppdrag-public-demo-assets | Bucket public detecte. | Activer Block Public Access et limiter les policies au besoin exact. |
| S3-001 | HIGH | oppdrag-analytics-snapshots | Bucket public detecte. | Activer Block Public Access et limiter les policies au besoin exact. |
| S3-002 | MEDIUM | oppdrag-client-exports | Chiffrement au repos desactive. | Activer SSE-S3 ou SSE-KMS. |
| S3-002 | MEDIUM | oppdrag-raw-ingest | Chiffrement au repos desactive. | Activer SSE-S3 ou SSE-KMS. |
| S3-002 | MEDIUM | oppdrag-analytics-snapshots | Chiffrement au repos desactive. | Activer SSE-S3 ou SSE-KMS. |
| S3-002 | MEDIUM | oppdrag-backups | Chiffrement au repos desactive. | Activer SSE-S3 ou SSE-KMS. |
| S3-002 | MEDIUM | oppdrag-temp-share | Chiffrement au repos desactive. | Activer SSE-S3 ou SSE-KMS. |
| S3-002 | MEDIUM | oppdrag-terraform-state | Chiffrement au repos desactive. | Activer SSE-S3 ou SSE-KMS. |
| S3-003 | LOW | oppdrag-public-demo-assets | Versioning desactive. | Activer le versioning pour faciliter restauration et forensic. |
| S3-003 | LOW | oppdrag-client-exports | Versioning desactive. | Activer le versioning pour faciliter restauration et forensic. |
| S3-003 | LOW | oppdrag-raw-ingest | Versioning desactive. | Activer le versioning pour faciliter restauration et forensic. |
| S3-003 | LOW | oppdrag-analytics-snapshots | Versioning desactive. | Activer le versioning pour faciliter restauration et forensic. |
| S3-003 | LOW | oppdrag-backups | Versioning desactive. | Activer le versioning pour faciliter restauration et forensic. |
| S3-003 | LOW | oppdrag-terraform-state | Versioning desactive. | Activer le versioning pour faciliter restauration et forensic. |

## Takeaways

- Les risques IAM et exposition reseau dominent les findings critiques.
- Un scoring contextualise rend la priorisation plus actionnable.
- Le rapport doit inclure la validation des corrections, pas seulement la detection.
