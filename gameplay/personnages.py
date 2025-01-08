class Personnage:
    def __init__(self, nom, classe, pv, force, defense):
        self.nom = nom
        self.classe = classe
        self.pv = pv
        self.force = force
        self.defense = defense

    def attaquer(self, cible):
        """Le personnage attaque une cible."""
        degats = max(0, self.force - cible.defense)
        cible.pv -= degats
        print(f"{self.nom} inflige {degats} points de dégâts à {cible.nom}!")

    def est_vivant(self):
        """Vérifie si le personnage est toujours en vie."""
        return self.pv > 0
