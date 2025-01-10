class Ennemi:
    def __init__(self, nom, pv, attaque_min, attaque_max, xp_donne):
        self.nom = nom
        self.pv = pv
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max
        self.xp_donne = xp_donne


def creer_ennemi(type_ennemi):
    if type_ennemi == "Gobelin":
        return Ennemi("Gobelin", 30, 3, 7, 20)
    elif type_ennemi == "Dragon":
        return Ennemi("Dragon", 100, 10, 20, 100)
