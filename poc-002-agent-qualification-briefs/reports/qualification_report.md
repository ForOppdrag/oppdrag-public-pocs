# Rapport POC-002 - Agent qualification briefs

Briefs testes: 5
Completude initiale moyenne: 63%
Completude apres clarification (simulee : +15,5 points par question posee, aucune reponse obtenue): 94%

| Brief | Domaine | Initial | Simulee | Budget | Champs manquants |
| --- | --- | ---: | ---: | --- | --- |
| brief-001 | IA | 83% | 98% | 850 EUR/j | constraints |
| brief-002 | IA | 50% | 96% | a clarifier | duration, location, budget |
| brief-003 | IA | 67% | 98% | a clarifier | location, budget |
| brief-004 | IA | 33% | 80% | a clarifier | role, duration, location, constraints |
| brief-005 | DATA | 83% | 98% | a clarifier | constraints |

## Questions de clarification generees

### brief-001
- Quelles contraintes de securite, conformite ou delai sont bloquantes ?
### brief-002
- Quelle duree cible et quel rythme de mission faut-il prevoir ?
- Quel mode de travail est attendu : remote, hybride ou sur site ?
- Quel budget ou TJM plafond est valide pour ce besoin ?
### brief-003
- Quel mode de travail est attendu : remote, hybride ou sur site ?
- Quel budget ou TJM plafond est valide pour ce besoin ?
### brief-004
- Quel profil exact doit etre priorise pour cette mission ?
- Quelle duree cible et quel rythme de mission faut-il prevoir ?
- Quel mode de travail est attendu : remote, hybride ou sur site ?
### brief-005
- Quelles contraintes de securite, conformite ou delai sont bloquantes ?

## Takeaways

- Detection des rubriques par mots-cles, sans agent ni modele de langage.
- La completude apres clarification est simulee : aucune question n'a recu de reponse.
- La detection par sous-chaines est fragile : le mot-cle 'ia' classe a tort les briefs 001 (donnee) et 003 (securite) en IA.
