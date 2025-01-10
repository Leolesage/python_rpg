import random

def combat_tour_par_tour(joueur, ennemi):
    print(f"\n🔥 Combat engagé contre {ennemi.nom} (PV : {ennemi.pv}) !")

    while joueur.pv > 0 and ennemi.pv > 0:
        print(f"\n🎮 {joueur.nom} (PV : {joueur.pv}) VS {ennemi.nom} (PV : {ennemi.pv})")
        print("1. Attaquer")
        print("2. Utiliser une potion")
        print("3. Fuir")
        action = input("Votre choix : ")

        if action == "1":
            degats = random.randint(joueur.attaque_min, joueur.attaque_max)
            ennemi.pv -= degats
            print(f"Vous infligez {degats} dégâts à {ennemi.nom} !")
        elif action == "2":
            joueur.utiliser_potion()
        elif action == "3":
            chance_fuite = random.randint(1, 100)
            if chance_fuite > 50:
                print("🏃 Vous avez réussi à fuir le combat !")
                return
            else:
                print("❌ Échec de la fuite ! L'ennemi attaque.")
        else:
            print("Action invalide ! L'ennemi en profite pour attaquer.")

        if ennemi.pv > 0:
            degats = random.randint(ennemi.attaque_min, ennemi.attaque_max)
            joueur.pv -= degats
            print(f"{ennemi.nom} vous inflige {degats} dégâts !")

    if joueur.pv <= 0:
        print("💀 Vous avez été vaincu...")
    elif ennemi.pv <= 0:
        print(f"🎉 Vous avez vaincu {ennemi.nom} !")
        joueur.gagner_xp(ennemi.xp_donne)
