def afficher_inventaire(joueur):
    print("\n=== INVENTAIRE ===")
    print(f"Potions : {joueur.potions}")

def utiliser_potion(joueur):
    if joueur.potions > 0:
        joueur.utiliser_potion()
    else:
        print("Vous n'avez pas de potions dans votre inventaire !")