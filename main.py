from gameplay.personnages import Joueur
from gameplay.ennemis import Gobelin, Boss
from gameplay.combat import combat
from gameplay.exploration import explorer
from utils.affichage import afficher_statistiques
from utils.sauvegarde import sauvegarder_partie, charger_partie

def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Nouvelle Partie")
    print("2. Charger une Partie")
    print("3. Quitter")
    choix = input("Votre choix : ")
    return choix

def nouvelle_partie():
    print("\n=== NOUVELLE PARTIE ===")
    # Demander au joueur de définir son nom
    nom = input("Entrez le nom de votre héros : ")
    joueur = Joueur(nom)
    print(f"\nBienvenue, {joueur.nom} le Guerrier !")
    return joueur

def charger_ou_nouvelle_partie():
    while True:
        choix = menu_principal()
        if choix == "1":
            return nouvelle_partie(), []
        elif choix == "2":
            try:
                joueur, ennemis_tues = charger_partie()
                print("\n=== PARTIE CHARGÉE ===")
                print(f"Bienvenue de retour, {joueur.nom} !")
                return joueur, ennemis_tues
            except FileNotFoundError:
                print("Aucune sauvegarde trouvée. Veuillez démarrer une nouvelle partie.")
        elif choix == "3":
            print("Au revoir !")
            exit()
        else:
            print("Choix invalide, veuillez réessayer.")

def jeu():
    joueur, ennemis_tues = charger_ou_nouvelle_partie()
    ennemis_tues_count = len(ennemis_tues)

    while True:
        print("\n=== MENU DE JEU ===")
        print("1. Explorer")
        print("2. Afficher les Statistiques")
        print("3. Sauvegarder et Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            ennemi = explorer(ennemis_tues_count)
            if ennemi:
                print(f"\nUn {ennemi.nom} sauvage apparaît !")
                resultat = combat(joueur, ennemi)
                if resultat == "fuite":
                    print("Vous avez fui le combat.")
                elif resultat == "victoire":
                    ennemis_tues.append(ennemi)
                    ennemis_tues_count += 1
                    print(f"Vous avez vaincu {ennemi.nom} !")
                    joueur.gagner_xp(ennemi.xp_donne)
                    
                    # Vérifier si le boss doit apparaître
                    if ennemis_tues_count == 10:  # Déclenche le boss après 10 gobelins tués
                        print("\n=== LE BOSS APPARAÎT ! ===")
                        boss = Boss()
                        print(f"Un {boss.nom} apparaît ! Préparez-vous au combat final !")
                        if combat(joueur, boss) == "victoire":
                            print(f"Félicitations, {joueur.nom} ! Vous avez vaincu le boss et terminé le jeu !")
                            break
                        else:
                            print("Le boss vous a vaincu... Fin de la partie.")
                            break
                elif resultat == "defaite":
                    print("Vous êtes mort. Fin de la partie.")
                    break
        elif choix == "2":
            afficher_statistiques(joueur)
        elif choix == "3":
            sauvegarder_partie(joueur, ennemis_tues)
            print("Partie sauvegardée. À bientôt !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    jeu()
