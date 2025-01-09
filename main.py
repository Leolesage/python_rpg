from gameplay.personnages import Personnage
from gameplay.exploration import explorer
from gameplay.statisques import afficher_statistiques
from gameplay.inventaire import afficher_inventaire

def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Nouvelle Partie")
    print("2. Charger une Partie")
    print("3. Quitter")
    choix = input("Votre choix : ")
    return choix

def jeu():
    joueur = Personnage()

    while True:
        choix = menu_principal()
        if choix == "1":
            nom_joueur = input("Entrez le nom de votre héros : ").strip()
            if not nom_joueur:
                nom_joueur = "Héros"  
            joueur = joueur(nom=nom_joueur)
            print(f"\nBienvenue, {joueur.nom} le Guerrier !")
            while joueur.pv > 0:
                print("\n1. Explorer")
                print("2. Afficher les statistiques")
                print("3. Afficher l'inventaire")
                print("4. Quitter")
                action = input("Votre choix : ")

                if action == "1":
                    explorer(joueur)
                elif action == "2":
                    afficher_statistiques(joueur)
                elif action == "3":
                    afficher_inventaire(joueur)
                elif action == "4":
                    print("Merci d'avoir joué !")
                    break
                else:
                    print("Choix invalide.")
        elif choix == "3":
            print("Au revoir !")
            break

if __name__ == "__main__":
    jeu()