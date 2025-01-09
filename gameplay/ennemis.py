class Ennemi:
    """
    Classe représentant un ennemi.
    """
    def __init__(self, nom, pv, attaque_min, attaque_max, xp_donne):
        self.nom = nom
        self.pv = pv
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max
        self.xp_donne = xp_donne

    def attaquer(self):
        import random
        return random.randint(self.attaque_min, self.attaque_max)

    def recevoir_degats(self, degats):
        self.pv -= degats
        print(f"{self.nom} reçoit {degats} points de dégâts.")


def creer_ennemi(type_ennemi):
    if type_ennemi == "Gobelin":
        return Ennemi(nom="Gobelin", pv=50, attaque_min=5, attaque_max=10, xp_donne=20)
    elif type_ennemi == "Dragon":
        return Ennemi(nom="Dragon", pv=150, attaque_min=20, attaque_max=30, xp_donne=100)
    else:
        raise ValueError(f"Type d'ennemi inconnu : {type_ennemi}")