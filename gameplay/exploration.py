from gameplay.personnages import Joueur
from gameplay.ennemis import Gobelin, Boss
from gameplay.combat import combat_tour_par_tour
import random

def explorer(joueur, gobelins_tues):
    print("Vous explorez les environs...")
    rencontre = random.choice(["gobelin", "rien"])
    
    if rencontre == "gobelin":
        print("Vous rencontrez un Gobelin !")
        ennemi = Gobelin()
        combat_termine = combat_tour_par_tour(joueur, ennemi)
        if not combat_termine:
            gobelins_tues += 1
            print(f"Gobelins vaincus : {gobelins_tues}")
    else:
        print("Rien à signaler lors de votre exploration.")
    
    # Si 10 gobelins vaincus, invoquer le boss
    if gobelins_tues == 10:
        print("⚠️ Un puissant ennemi approche... Le BOSS FINAL apparaît ! ⚠️")
        boss = Boss()
        combat_termine = combat_tour_par_tour(joueur, boss, boss=True)
        if combat_termine:
            return True, gobelins_tues  # Fin du jeu
    return False, gobelins_tues
