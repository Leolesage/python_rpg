from gameplay.personnages import Personnage

def lancer_combat(joueur, ennemi):
    """Simule un combat entre le joueur et un ennemi."""
    print(f"Un combat commence entre {joueur.nom} et {ennemi.nom} !")
    
    while joueur.est_vivant() and ennemi.est_vivant():
        # Tour du joueur
        joueur.attaquer(ennemi)
        if not ennemi.est_vivant():
            print(f"{ennemi.nom} est vaincu !")
            return "victoire"

        # Tour de l'ennemi
        ennemi.attaquer(joueur)
        if not joueur.est_vivant():
            print(f"{joueur.nom} a été vaincu...")
            return "défaite"
