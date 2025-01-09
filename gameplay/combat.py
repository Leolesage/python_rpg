import random

def combat_tour_par_tour(joueur, ennemi, boss=False):
    if boss:
        print(f"⚔️ Un combat épique commence contre le BOSS FINAL : {ennemi.nom} ! ⚔️")
    else:
        print(f"Un combat commence entre {joueur.nom} et {ennemi.nom} !")

    while joueur.pv > 0 and ennemi.pv > 0:
        # Tour du joueur
        print("\n=== TOUR DU JOUEUR ===")
        print("1. Attaquer  2. Utiliser une potion  3. Fuir" if not boss else "1. Attaquer  2. Utiliser une potion")
        action = input("Votre choix : ")
        if action == "1":
            degats = random.randint(joueur.attaque_min, joueur.attaque_max)
            ennemi.pv -= degats
            print(f"Vous infligez {degats} dégâts à {ennemi.nom} (PV restant : {max(ennemi.pv, 0)})")
        elif action == "2":
            joueur.utiliser_potion()
        elif action == "3" and not boss:  # Pas de fuite possible contre le boss
            chance_de_fuite = random.randint(1, 100)
            if chance_de_fuite <= 50:  # 50% de chances de fuir
                print(f"Vous réussissez à fuir le combat contre {ennemi.nom} !")
                return False  # Le joueur quitte le combat
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
            if boss:
                print("🎉✨ Vous avez vaincu le BOSS FINAL et terminé le jeu ! Félicitations ! ✨🎉")
                return True  # Fin du jeu
            joueur.gagner_xp(ennemi.xp_donne)
            return False

        # Tour de l'ennemi
        print("\n=== TOUR DE L'ENNEMI ===")
        degats = random.randint(ennemi.attaque_min, ennemi.attaque_max)
        joueur.pv -= degats
        print(f"{ennemi.nom} vous inflige {degats} dégâts (PV restant : {max(joueur.pv, 0)})")

        # Vérification si le joueur est mort
        if joueur.pv <= 0:
            print("Vous êtes mort ! Game Over.")
            return True
