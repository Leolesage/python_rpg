from gameplay.personnages import Personnage
from gameplay.exploration import explorer
from gameplay.inventaire import afficher_inventaire
from gameplay.statisques import afficher_statistiques
from sauvegarder import Sauvegarde

sauvegarde = Sauvegarde()  # Initialise l'objet Sauvegarde

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
        print("4. Sauvegarder la partie")
        print("5. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            explorer(joueur)
        elif choix == "2":
            afficher_inventaire(joueur)
        elif choix == "3":
            afficher_statistiques(joueur)
        elif choix == "4":
            sauvegarde.sauvegarder_joueur(joueur)  # Sauvegarde le joueur
        elif choix == "5":
            print("Fin de la session de jeu.")
            break
        else:
            print("Choix invalide. Réessayez.")

def nouvelle_partie():
    pseudo = input("Entrez votre pseudo : ").strip()
    if not pseudo:
        pseudo = "Héros"  # Nom par défaut si le joueur ne saisit rien
    joueur = Personnage(pseudo)
    print(f"Bienvenue, {joueur.nom} ! Vous commencez avec {joueur.pv} PV.")
    menu_jeu(joueur)

def charger_partie():
    sauvegarde.afficher_sauvegardes()  # Affiche les sauvegardes disponibles
    pseudo = input("\nEntrez le pseudo du joueur à charger : ").strip()
    data_joueur = sauvegarde.charger_joueur(pseudo)

    if data_joueur:
        # Crée une instance de Personnage avec les données chargées
        joueur = Personnage(nom=data_joueur["nom"])
        joueur.pv = data_joueur["pv"]
        joueur.niveau = data_joueur["niveau"]
        joueur.xp = data_joueur["xp"]
        joueur.xp_niveau_suivant = data_joueur["xp_niveau_suivant"]
        joueur.attaque_min = data_joueur["attaque_min"]
        joueur.attaque_max = data_joueur["attaque_max"]
        joueur.potions = data_joueur["potions"]

        print(f"Bienvenue de retour, {joueur.nom} !")
        menu_jeu(joueur)
    else:
        print(" Aucun joueur trouvé avec ce pseudo. Retour au menu principal.")

def main():
    while True:
        choix = menu_principal()

        if choix == "1":
            nouvelle_partie()
        elif choix == "2":
            charger_partie()
        elif choix == "3":
            print("À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
