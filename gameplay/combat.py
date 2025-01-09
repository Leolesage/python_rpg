import random

def combat_tour_par_tour(joueur, ennemi):
    print(f"Un combat commence entre {joueur.nom} et {ennemi.nom} !")

    while joueur.pv > 0 and ennemi.pv > 0:
        # Tour du joueur
        print("\n=== TOUR DU JOUEUR ===")
        action = input("1. Attaquer  2. Utiliser une potion : ")
        if action == "1":
            degats = random.randint(joueur.attaque_min, joueur.attaque_max)
            ennemi.pv -= degats
            print(f"Vous infligez {degats} dégâts à {ennemi.nom} (PV restant : {max(ennemi.pv, 0)})")
        elif action == "2":
            joueur.utiliser_potion()
        else:
            print("Action invalide ! Vous perdez votre tour.")

        # Vérification si l'ennemi est mort
        if ennemi.pv <= 0:
            print(f"Vous avez vaincu {ennemi.nom} ! ")
            joueur.gagner_xp(ennemi.xp_donne)
            return

        # Tour de l'ennemi
        print("\n=== TOUR DE L'ENNEMI ===")
        degats = random.randint(ennemi.attaque_min, ennemi.attaque_max)
        joueur.pv -= degats
        print(f"{ennemi.nom} vous inflige {degats} dégâts (PV restant : {max(joueur.pv, 0)})")

        # Vérification si le joueur est mort
        if joueur.pv <= 0:
            print("Vous êtes mort ! Game Over.")
            return
