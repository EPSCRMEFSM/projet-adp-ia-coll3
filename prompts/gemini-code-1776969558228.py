from datetime import datetime

# Données de l'analyse
content = """ANALYSE DU RÉFÉRENTIEL : NATATION DE VITESSE (DNB)
NOM DU FICHIER : Analyse_Ref_natation_vitesse_EquipeN_ADP2026
DATE : 23/04/2026
------------------------------------------------------------------

[1] RÔLE IA
Enseignant EPS expert en didactique des APS, spécialiste du référentiel B.O. n°5 du 19 juillet 2012.

[2] CONTEXTE
APS         : Natation de vitesse
Famille     : Activités de performance motrice (Athlétisme/Natation)
Niveau      : Niveau 2
Population  : Collégiens (3ème - Diplôme National du Brevet)

[3] TABLEAU D'ANALYSE DU RÉFÉRENTIEL

CRITÈRE 1 : Performance au 50 m deux nages (8 points)
- Indicateurs : Chronométrage (25m ventral + 25m dorsal)
- Degré A (8 pts) : F <= 42" | G <= 37"
- Degré B (5 pts) : F = 56"  | G = 51"
- Degré C (2 pts) : F >= 1'20" | G >= 1'15"

CRITÈRE 2 : Efficacité du rapport amplitude/fréquence (8 points)
- Indicateurs : Nombre de cycles de bras sur 50 m
- Degré A (6,5 - 8 pts) : "Nageur glisseur propulseur" (moins de 30 cycles)
- Degré B (4,5 - 6 pts) : "Nageur aquatique énergétique" (de 30 à 35 cycles)
- Degré C (0 - 4 pts)   : "Nageur bagarreur" (plus de 35 cycles)

CRITÈRE 3 : Efficacité du starter, du chronométreur, et de l'observateur (4 points)
- Indicateurs : Respect des commandements, précision, conseils
- Degré A (3,5 - 4 pts) : "Au juge multifonctions" (régularité, écart < 2 dixièmes, conseils pertinents)
- Degré B (2 - 3 pts)     : "Au juge fiable" (respect des commandements, écart 2 à 3 dixièmes)
- Degré C (0 - 1,5 pts)   : "Du juge dilettante" (règlement non respecté, écart > 3 dixièmes)

------------------------------------------------------------------
[4] SPÉCIFICITÉS TERRAIN À INTÉGRER
- Épreuve : 25m ventral puis 25m dorsal.
- Rôles : Nageur, starter, observateur, chronométreur (rotation obligatoire).
- Cycle de bras : 2 coups de bras (crawl/dos) ou 1 mouvement (brasse).
- Abandon : 0,5 pt par tranche de 12,5m parcourue.
- Barème : Différencié Filles / Garçons.

------------------------------------------------------------------
[5] SECTION F : NOTES DE L'ÉQUIPE (LOG DE L'IA)
* Ce qui a fonctionné : Conversion fidèle des données visuelles du B.O. en format texte structuré.
* Ce qui a été ajusté : Passage de "Course de vitesse" à "Natation de vitesse" suite à la réception du document source.
* Règle respectée : Utilisation stricte de la terminologie officielle ("Juge multifonctions", "Nageur bagarreur").
"""

filename = "Analyse_Ref_Natation_Vitesse_ADP2026.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(content)