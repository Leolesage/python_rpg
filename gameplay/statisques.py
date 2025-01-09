def afficher_statistiques(joueur):
    print("\n=== STATISTIQUES DU JOUEUR ===")
    print(f"Nom : {joueur.nom}")
    print(f"Points de Vie (PV) : {joueur.pv}")
    print(f"Attaque : {joueur.attaque_min} - {joueur.attaque_max}")
    print(f"Niveau : {joueur.niveau}")
    print(f"Expérience : {joueur.xp} / {joueur.xp_niveau_suivant}")