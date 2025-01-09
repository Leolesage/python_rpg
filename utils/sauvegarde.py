import json

def sauvegarder(joueur):
    """Sauvegarde les données du joueur dans un fichier JSON."""
    with open("sauvegarde.json", "w") as fichier:
        json.dump({
            "nom": joueur.nom,
            "classe": joueur.classe,
            "pv": joueur.pv,
            "force": joueur.force,
            "defense": joueur.defense,
            "xp": joueur.xp,
            "xp_niveau": joueur.xp_niveau,
            "niveau": joueur.niveau,
            "position": joueur.position,
        }, fichier)
    print("Partie sauvegardée !")

def charger():
    """Charge les données du joueur depuis un fichier JSON."""
    try:
        with open("sauvegarde.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None