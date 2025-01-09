from gameplay.personnages import Joueur
from gameplay.exploration import explorer
from utils.affichage import afficher_statistiques
from utils.sauvegarde import sauvegarder_partie, charger_partie

def main():
    print("=== MENU PRINCIPAL ===")
    print("1. Nouvelle Partie")
    print("2. Charger une Partie")
    print("3. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Entrez le nom de votre héros : ")
        joueur = Joueur(nom)
        gobelins_tues = 0
        print(f"Bienvenue, {joueur.nom} le Guerrier !")
    elif choix == "2":
        joueur, gobelins_tues = charger_partie()
        print(f"Chargement de la partie... Bienvenue de retour, {joueur.nom} !")
    elif choix == "3":
        print("À bientôt !")
        return
    else:
        print("Choix invalide.")
        return

    jeu_termine = False
    while not jeu_termine and joueur.pv > 0:
        print("\n=== MENU ===")
        print("1. Explorer")
        print("2. Voir les statistiques")
        print("3. Sauvegarder la partie")
        print("4. Quitter")
        action = input("Votre choix : ")

        if action == "1":
            jeu_termine, gobelins_tues = explorer(joueur, gobelins_tues)
        elif action == "2":
            afficher_statistiques(joueur)
        elif action == "3":
            sauvegarder_partie(joueur, gobelins_tues)
        elif action == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
    
    if jeu_termine:
        print("Merci d'avoir joué à ce RPG !")
