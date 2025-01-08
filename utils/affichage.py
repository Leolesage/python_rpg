def afficher_statistiques(joueur):
    """Affiche les statistiques du joueur."""
    print("\n=== STATISTIQUES ===")
    print(f"Nom : {joueur.nom}")
    print(f"Classe : {joueur.classe}")
    print(f"PV : {joueur.pv}")
    print(f"Force : {joueur.force}")
    print(f"Défense : {joueur.defense}")
    print(f"XP : {joueur.get('xp', 0)} / {joueur.get('xp_niveau', 100)}")
