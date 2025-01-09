import random
from personnages import utiliser_potion

def combat_tour_par_tour(joueur, ennemi):
    print(f"Un combat commence entre {joueur.nom} et {ennemi.nom} !")

    while joueur.pv > 0 and ennemi.pv > 0:
        # Tour du joueur
        print("\n=== TOUR DU JOUEUR ===")
        print("1. Attaquer  2. Utiliser une potion  3. Fuir")
        action = input("Votre choix : ")
        if action == "1":
            degats = random.randint(joueur.attaque_min, joueur.attaque_max)
            ennemi.pv -= degats
            print(f"Vous infligez {degats} dégâts à {ennemi.nom} (PV restant : {max(ennemi.pv, 0)})")
        elif action == "2":
            joueur.utiliser_potion()
        elif action == "3":
            chance_de_fuite = random.randint(1, 100)
            if chance_de_fuite <= 50:  # 50% de chances de fuir
                print(f"Vous réussissez à fuir le combat contre {ennemi.nom} !")
                return  # Le joueur quitte le combat
            else:
                print(f"La fuite échoue ! {ennemi.nom} vous attaque pendant votre tentative.")
                degats = random.randint(ennemi.attaque_min, ennemi.attaque_max)
                joueur.pv -= degats
                print(f"{ennemi.nom} inflige {degats} dégâts pendant votre fuite (PV restant : {max(joueur.pv, 0)})")
        else:
            print("Action invalide ! Vous perdez votre tour.")

        # Vérification si l'ennemi est mort
        if ennemi.pv <= 0:
            print(f"Vous avez vaincu {ennemi.nom} ! 🎉")
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