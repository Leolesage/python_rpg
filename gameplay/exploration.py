import random
from gameplay.ennemis import creer_ennemi
from gameplay.combat import combat_tour_par_tour


def explorer(joueur):
    print("\n=== EXPLORATION ===")
    evenements = ["combat", "objet", "rien"]
    evenement = random.choice(evenements)

    if evenement == "combat":
        ennemi_type = random.choice(["Gobelin", "Dragon"])
        ennemi = creer_ennemi(ennemi_type)
        print(f"Vous avez rencontré un {ennemi.nom} ! Préparez-vous au combat.")
        combat_tour_par_tour(joueur, ennemi)

    elif evenement == "objet":
        objet = random.choice(["Potion", "Équipement"])
        if objet == "Potion":
            joueur.potions += 1
            print("Vous trouvez une potion et la rangez dans votre sac !")
        elif objet == "Équipement":
            joueur.attaque_min += 2
            joueur.attaque_max += 5
            print("Vous trouvez une nouvelle arme qui augmente vos dégâts !")

    elif evenement == "rien":
        print("Rien d'intéressant ici... Vous continuez votre chemin.")