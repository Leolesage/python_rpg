class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.pv = 100
        self.attaque_min = 10
        self.attaque_max = 20
        self.niveau = 1
        self.experience = 0
        self.potions = 3

    def utiliser_potion(self):
        if self.potions > 0:
            self.pv += 50
            self.potions -= 1
            print(f"Vous avez utilisé une potion. PV : {self.pv}, Potions restantes : {self.potions}")
        else:
            print("Vous n'avez plus de potions !")

    def gagner_xp(self, xp):
        self.experience += xp
        print(f"Vous gagnez {xp} points d'expérience ! Total : {self.experience}")
        if self.experience >= self.niveau * 100:
            self.experience -= self.niveau * 100
            self.niveau += 1
            self.pv += 20
            self.attaque_min += 2
            self.attaque_max += 5
            print(f"🎉 Vous avez atteint le niveau {self.niveau} !")
