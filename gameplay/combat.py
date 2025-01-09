def combat_tour_par_tour(joueur, ennemi):
    print("\n=== COMBAT TOUR PAR TOUR ===")
    print(f"Un {ennemi.nom} sauvage apparait avec {ennemi.pv} PV !")

    while joueur.pv > 0 and ennemi.pv > 0:
        # Tour du joueur
        print("\n--- Tour du Joueur ---")
        print("1. Attaquer")
        print("2. Utiliser une potion")
        print("3. Fuir")
        choix = input("Votre choix : ")

        if choix == "1":
            degats = joueur.attaquer()
            ennemi.recevoir_degats(degats)
        elif choix == "2":
            joueur.utiliser_potion()
        elif choix == "3":
            print("Vous fuyez le combat...")
            return
        else:
            print("Action invalide.")

        if ennemi.pv <= 0:
            print(f"Vous avez vaincu {ennemi.nom} !")
            joueur.xp += ennemi.xp_donne
            print(f"Vous gagnez {ennemi.xp_donne} XP.")
            return

        # Tour de l'ennemi
        print("\n--- Tour de l'Ennemi ---")
        degats = ennemi.attaquer()
        joueur.recevoir_degats(degats)

        if joueur.pv <= 0:
            print("Vous êtes vaincu !")
            return