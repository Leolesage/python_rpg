class Personnage:
    def __init__(self, nom, classe, pv, force, defense):
        self.nom = nom
        self.classe = classe
        self.pv = pv
        self.force = force
        self.defense = defense
        self.xp = 0
        self.xp_niveau = 100
        self.niveau = 1
        self.position = {"x": 0, "y": 0}

    def est_vivant(self):
        """Retourne True si le personnage est toujours en vie."""
        return self.pv > 0

    def attaquer(self, cible):
        """Attaque une cible (autre personnage)."""
        degats = self.force - cible.defense
        if degats > 0:
            cible.pv -= degats
            print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts.")
        else:
            print(f"{self.nom} attaque {cible.nom} mais ne lui inflige aucun dégât.")
