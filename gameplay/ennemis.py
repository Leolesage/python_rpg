from gameplay.personnages import Personnage

def creer_ennemi_de_base():
    """Création d'un ennemi basique."""
    return Personnage(nom="Gobelin", classe="Monstre", pv=50, force=15, defense=5)

def creer_ennemi_boss():
    """Création d'un boss."""
    return Personnage(nom="Dragon", classe="Boss", pv=300, force=50, defense=20)