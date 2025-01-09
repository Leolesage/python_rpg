class Personnage:
    def __init__(self, nom, pv, attaque_min, attaque_max):
        self.nom = nom
        self.pv = pv
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max

    def est_mort(self):
        return self.pv <= 0


class Joueur(Personnage):
    def __init__(self, nom):
        super().__init__(nom, 100, 5, 10)
        self.niveau = 1
        self.xp = 0
        self.xp_niveau_suivant = 100
        self.potions = 3

    def utiliser_potion(self):
        if self.potions > 0:
            self.pv += 30
            self.potions -= 1
            print(f"{self.nom} utilise une potion. PV restaurés : {self.pv} (Potions restantes : {self.potions})")
        else:
            print("Vous n'avez plus de potions !")

    def gagner_xp(self, xp_gagne):
        self.xp += xp_gagne
        print(f"\n{self.nom} gagne {xp_gagne} points d'expérience !")

        while self.xp >= self.xp_niveau_suivant:
            self.xp -= self.xp_niveau_suivant
            self.niveau += 1
            self.xp_niveau_suivant += 50
            self.pv += 20
            self.attaque_min += 2
            self.attaque_max += 3
            print(f" {self.nom} monte au niveau {self.niveau} !")

    
