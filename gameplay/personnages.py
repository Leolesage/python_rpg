class Personnage:
    """
    Classe représentant le joueur dans le jeu.
    """
    def init(self, nom="Héros", pv=100, attaque_min=10, attaque_max=20, potions=3, niveau=1):
        self.nom = nom
        self.pv = pv
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max
        self.potions = potions
        self.xp = 0
        self.niveau = niveau
        self.defense_active = False

    def attaquer(self):
        import random
        return random.randint(self.attaque_min, self.attaque_max)

    def utiliser_potion(self):
        if self.potions > 0:
            self.pv += 20
            self.potions -= 1
            print(f"{self.nom} utilise une potion et récupère 20 PV.")
        else:
            print(f"{self.nom} n'a plus de potions !")

    def activer_defense(self):
        self.defense_active = True
        print(f"{self.nom} se met en position défensive.")

    def recevoir_degats(self, degats):
        if self.defense_active:
            degats = max(0, degats // 2)
            self.defense_active = False
        self.pv -= degats
        print(f"{self.nom} reçoit {degats} points de dégâts.")