import json

def sauvegarder(progression, fichier="sauvegarde.json"):
    """Sauvegarde la progression dans un fichier JSON."""
    with open(fichier, "w") as f:
        json.dump(progression, f)  # Sérialise les données en JSON
    print("Partie sauvegardée avec succès !")

def charger(fichier="sauvegarde.json"):
    """Charge une partie depuis un fichier JSON."""
    try:
        with open(fichier, "r") as f:
            progression = json.load(f)  # Désérialise les données JSON en Python
        print("Partie chargée avec succès !")
        return progression
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée. Lancez une nouvelle partie.")
        return None
