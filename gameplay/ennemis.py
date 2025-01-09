class Ennemi:
    def __init__(self, nom, pv, attaque_min, attaque_max, xp_donne):
        """
        Représente un ennemi avec ses statistiques.
        """
        self.nom = nom
        self.pv = pv
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max
        self.xp_donne = xp_donne


def creer_ennemi(type_ennemi):
    """
    Crée un ennemi basé sur son type.
    :param type_ennemi: Type de l'ennemi ("Gobelin", "Dragon", etc.).
    :return: Instance de Ennemi.
    """
    if type_ennemi == "Gobelin":
        return Ennemi(nom="Gobelin", pv=30, attaque_min=5, attaque_max=10, xp_donne=50)
    elif type_ennemi == "Dragon":
        return Ennemi(nom="Dragon", pv=100, attaque_min=15, attaque_max=25, xp_donne=200)
    else:
        raise ValueError(f"Type d'ennemi inconnu : {type_ennemi}")
