from gameplay.personnages import Personnage
from gameplay.ennemis import creer_ennemi_de_base
from gameplay.combat import lancer_combat
from gameplay.exploration import deplacer
from gameplay.inventaire import Inventaire
from utils.sauvegarde import sauvegarder, charger
from utils.affichage import afficher_statistiques

def menu_principal():
    """Affiche le menu principal et retourne le choix de l'utilisateur."""
    print("\n=== MENU PRINCIPAL ===")
    print("1. Nouvelle Partie")
    print("2. Charger une Partie")
    print("3. Quitter")
    choix = input("Votre choix : ")
    return choix

def nouvelle_partie():
    """Lance une nouvelle partie."""
    joueur = {
        "nom": "Héros",
        "classe": "Guerrier",
        "pv": 100,
        "force": 20,
        "defense": 10,
        "xp": 0,
        "xp_niveau": 100,
        "inventaire": ["épée", "potion", "bouclier"],
        "position": {"x": 0, "y": 0},
        "niveau": 1,
    }
    print(f"Bienvenue, {joueur['nom']} le {joueur['classe']} !")
    return joueur

def relancer_partie():
    """Charge une partie existante."""
    progression = charger()
    if progression:
        print(f"Partie rechargée ! Bonjour, {progression['nom']} le {progression['classe']} !")
    return progression

def gagner_xp(joueur, quantite):
    """Ajoute de l'XP au joueur et gère le passage de niveau."""
    joueur["xp"] += quantite
    print(f"Vous gagnez {quantite} points d'XP.")

    if joueur["xp"] >= joueur["xp_niveau"]:
        joueur["xp"] -= joueur["xp_niveau"]
        joueur["xp_niveau"] = int(joueur["xp_niveau"] * 1.5)
        joueur["niveau"] += 1
        print(f"Félicitations ! Vous passez au niveau {joueur['niveau']} !")
        joueur["pv"] += 20
        joueur["force"] += 5
        joueur["defense"] += 3

if __name__ == "__main__":
    joueur = None
    inventaire = Inventaire()

    while True:
        choix = menu_principal()
        if choix == "1":
            joueur = nouvelle_partie()
            afficher_statistiques(joueur)
        elif choix == "2":
            joueur = relancer_partie()
            if joueur:
                afficher_statistiques(joueur)
        elif choix == "3":
            print("À bientôt !")
            break
        else:
            print("Choix invalide.")
            continue

        # Gameplay principal
        while joueur and joueur["pv"] > 0:
            print("\n=== Actions disponibles ===")
            print("1. Explorer")
            print("2. Voir Inventaire")
            print("3. Sauvegarder et Quitter")
            action = input("Votre choix : ")

            if action == "1":
                direction = input("Direction (nord/sud/est/ouest) : ")
                joueur["position"] = deplacer(joueur["position"], direction)

                # Simuler un combat aléatoire
                ennemi = creer_ennemi_de_base()
                print(f"\nVous rencontrez un {ennemi.nom} !")
                resultat = lancer_combat(joueur, ennemi)

                if resultat == "victoire":
                    gagner_xp(joueur, 50)
                    inventaire.ajouter_objet("Trésor du gobelin")
                elif resultat == "défaite":
                    print("Vous avez perdu le combat...")
                    break

            elif action == "2":
                inventaire.afficher()

            elif action == "3":
                sauvegarder(joueur)
                print("Partie sauvegardée. À bientôt !")
                break

            else:
                print("Action invalide.")

        if joueur and joueur["pv"] <= 0:
            print("Game Over. Vous pouvez relancer une nouvelle partie.")
