class Ennemi:
    def __init__(self, nom, pv, attaque_min, attaque_max, xp_donne):
        self.nom = nom
        self.pv = pv
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max
        self.xp_donne = xp_donne

def creer_ennemi(type_ennemi, niveau_joueur):
    if type_ennemi == "Gobelin":
        return Ennemi(
            nom="Gobelin",
            pv=10 + niveau_joueur * 2,
            attaque_min=2 + niveau_joueur,
            attaque_max=5 + niveau_joueur,
            xp_donne=15 + niveau_joueur * 5
        )
    elif type_ennemi == "Dragon":
        return Ennemi(
            nom="Dragon",
            pv=50 + niveau_joueur * 10,
            attaque_min=10 + niveau_joueur * 2,
            attaque_max=15 + niveau_joueur * 2,
            xp_donne=50 + niveau_joueur * 20
        )
    else:
        raise ValueError("Type d'ennemi inconnu.")
