def afficher_inventaire(joueur):
    print("\n=== INVENTAIRE ===")
    print(f"Potions : {joueur.potions}")
    print(f"Armes : Attaque [{joueur.attaque_min} - {joueur.attaque_max}]")
    print(f"PV : {joueur.pv}")
    print(f"Mana : {joueur.mana}")


def utiliser_potion(joueur):
    if joueur.potions > 0:
        joueur.utiliser_potion()
    else:
        print("Vous n'avez pas de potions dans votre inventaire !")
