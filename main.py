from gameplay.personnages import Joueur
from gameplay.ennemis import Ennemi
from gameplay.exploration import Exploration
from utils.affichage import afficher_stats
from utils.sauvegarde import sauvegarder_partie, charger_partie

# Initialisation du jeu
def main():
    print("=== Bienvenue dans votre RPG Console ===")
    print("1. Nouvelle Partie")
    print("2. Charger une Partie")
    print("3. Quitter")
    
    choix = input("Votre choix : ")
    
    if choix == "1":
        nom_joueur = input("Entrez le nom de votre héros : ")
        joueur = Joueur(nom=nom_joueur)
        ennemis_tues = 0
    elif choix == "2":
        joueur, ennemis_tues = charger_partie()
        if not joueur:
            print("Aucune sauvegarde trouvée. Lancement d'une nouvelle partie.")
            nom_joueur = input("Entrez le nom de votre héros : ")
            joueur = Joueur(nom=nom_joueur)
            ennemis_tues = 0
    else:
        print("À bientôt !")
        return

    exploration = Exploration(joueur)
    boss = Ennemi("Dragon", 200, 15, 25, 100)

    while joueur.pv > 0:
        print("\n=== Menu Principal ===")
        print("1. Explorer")
        print("2. Afficher les statistiques")
        print("3. Sauvegarder et quitter")

        choix = input("Votre choix : ")
        
        if choix == "1":
            ennemi = exploration.explorer()
            if ennemi:
                joueur.combat(ennemi)
                if ennemi.est_mort():
                    ennemis_tues += 1
                    if ennemis_tues == 10:
                        print("\nLe BOSS FINAL apparaît ! Préparez-vous !")
                        joueur.combat(boss)
                        if boss.est_mort():
                            print("🎉 Vous avez vaincu le BOSS FINAL et terminé le jeu ! Félicitations ! 🎉")
                            break
        elif choix == "2":
            afficher_stats(joueur)
        elif choix == "3":
            sauvegarder_partie(joueur, ennemis_tues)
            print("Partie sauvegardée. À bientôt !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
