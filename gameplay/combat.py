import random

def combat_tour_par_tour(joueur, ennemi):
    """
    Gère un combat entre le joueur et un ennemi.
    """
    print(f"Le combat commence entre {joueur.nom} et {ennemi.nom} !")

    while joueur.pv > 0 and ennemi.pv > 0:
        # Tour du joueur
        print("\n=== TOUR DU JOUEUR ===")
        print("1. Attaquer")
        print("2. Utiliser une potion")
        action = input("Votre choix : ")

        if action == "1":
            degats = random.randint(joueur.attaque_min, joueur.attaque_max)
            ennemi.pv -= degats
            print(f"{joueur.nom} inflige {degats} dégâts à {ennemi.nom} (PV restant de {ennemi.nom} : {max(ennemi.pv, 0)})")
        elif action == "2":
            joueur.utiliser_potion()
        else:
            print("Action invalide ! Vous perdez votre tour.")

        # Vérifier si l'ennemi est mort
        if ennemi.pv <= 0:
            print(f"🎉 {joueur.nom} a vaincu {ennemi.nom} !")
            joueur.gagner_xp(ennemi.xp_donne)
            break

        # Tour de l'ennemi
        print("\n=== TOUR DE L'ENNEMI ===")
        degats = random.randint(ennemi.attaque_min, ennemi.attaque_max)
        joueur.pv -= degats
        print(f"{ennemi.nom} inflige {degats} dégâts à {joueur.nom} (PV restant : {max(joueur.pv, 0)})")

        # Vérifier si le joueur est mort
        if joueur.pv <= 0:
            print("💀 Vous êtes mort ! Game Over.")
            break
