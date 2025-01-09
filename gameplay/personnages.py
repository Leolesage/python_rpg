class Personnage:
    def __init__(self, nom="Héros"):
        self.nom = nom
        self.pv = 100
        self.attaque_min = 5
        self.attaque_max = 10
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
            self.xp_niveau_suivant += 50  # Augmenter le seuil pour le prochain niveau
            self.pv += 20
            self.attaque_min += 2
            self.attaque_max += 3
            print(f"{self.nom} monte au niveau {self.niveau} !")
            print(f"Stats actuelles : PV = {self.pv}, Attaque = {self.attaque_min}-{self.attaque_max}")

# Ajout de la classe Joueur pour éviter tout problème d'import
class Joueur(Personnage):
    def __init__(self, nom="Héros"):
        super().__init__(nom)
