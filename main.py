from gameplay.personnages import Personnage
from gameplay.exploration import explorer
from gameplay.inventaire import afficher_inventaire
from gameplay.ennemis import creer_ennemi
from gameplay.combat import combat_tour_par_tour
from gameplay.statisques import afficher_statistiques
from sauvegarder import Sauvegarde


def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Nouvelle Partie")
    print("2. Charger une Partie")
    print("3. Quitter")
    choix = input("Votre choix : ")
    return choix


def menu_jeu(joueur, sauvegarde):
    while True:
        print("\n=== MENU DU JEU ===")
        print("1. Explorer")
        print("2. Inventaire")
        print("3. Statistiques")
        print("4. Sauvegarder")
        print("5. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            explorer(joueur)
        elif choix == "2":
            afficher_inventaire(joueur)
        elif choix == "3":
            afficher_statistiques(joueur)
        elif choix == "4":
            sauvegarde.sauvegarder_joueur(joueur)
        elif choix == "5":
            print("Fin de la session de jeu.")
            break
        else:
            print("Choix invalide. Réessayez.")


def nouvelle_partie(sauvegarde):
    pseudo = input("Entrez votre pseudo : ")
    joueur = Personnage(pseudo)
    print(f"Bienvenue, {joueur.nom} ! Vous commencez avec {joueur.pv} PV et {joueur.mana} points de mana.")
    menu_jeu(joueur)

def charger_partie(sauvegarde):
    sauvegarde.afficher_sauvegardes()
    pseudo = input("Entrez le nom du joueur à charger : ")
    donnees_joueur = sauvegarde.charger_joueur(pseudo)
    if donnees_joueur:
        joueur = Personnage(**donnees_joueur)
        print(f"Partie chargée pour {joueur.nom}. Vous avez {joueur.pv} PV.")
        menu_jeu(joueur, sauvegarde)
    else:
        print("Erreur lors du chargement de la partie. Réessayez.")


def main():
    sauvegarde = Sauvegarde()
    while True:
        choix = menu_principal()

        if choix == "1":
            nouvelle_partie(sauvegarde)
        elif choix == "2":
            charger_partie(sauvegarde)
        elif choix == "3":
            print("À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
