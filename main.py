from gameplay.personnages import Personnage
from gameplay.exploration import explorer
from gameplay.inventaire import afficher_inventaire
from gameplay.ennemis import creer_ennemi
from gameplay.combat import combat_tour_par_tour
from utils.affichage import afficher_statistiques



def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Nouvelle Partie")
    print("2. Charger une Partie")
    print("3. Quitter")
    choix = input("Votre choix : ")
    return choix


def menu_jeu(joueur):
    while True:
        print("\n=== MENU DU JEU ===")
        print("1. Explorer")
        print("2. Inventaire")
        print("3. Statistiques")
        print("4. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            explorer(joueur)
        elif choix == "2":
            afficher_inventaire(joueur)
        elif choix == "3":
            afficher_statistiques(joueur)
        elif choix == "4":
            print("Fin de la session de jeu.")
            break
        else:
            print("Choix invalide. Réessayez.")
def nouvelle_partie():
    joueur = Personnage()
    print(f"Bienvenue, {joueur.nom} ! Vous commencez avec {joueur.pv} PV et {joueur.mana} points de mana.")
    menu_jeu(joueur)
def main():
    while True:
        choix = menu_principal()

        if choix == "1":
            nouvelle_partie()
        elif choix == "2":
            print("Chargement de la partie... (fonctionnalité à implémenter)")
        elif choix == "3":
            print("À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
if name == "main":
    main()