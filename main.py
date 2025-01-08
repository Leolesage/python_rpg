from gameplay.personnages import Personnage

def lancer_jeu():
    joueur = Personnage(nom="Héros", classe="Guerrier", pv=100, force=20, defense=10)
    print(f"Bienvenue, {joueur.nom} le {joueur.classe}!")
    return joueur

if __name__ == "__main__":
    joueur = lancer_jeu()
