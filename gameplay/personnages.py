import sqlite3

class Personnage:
    def __init__(self, nom):
        """
        Représente un personnage joueur avec ses statistiques.
        """
        self.nom = nom
        self.pv = 100
        self.attaque_min = 5
        self.attaque_max = 10
        self.niveau = 1
        self.xp = 0
        self.xp_niveau_suivant = 100
        self.potions = 3
    
    """def BDD(self):
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()
        insert_query = ""
        INSERT INTO users (nom, pv, xp, xp_niveau_suivant, attaque_min, attaque_max, potions)
        VALUES (?, ?, ?);
        ""
        
        users_data = [
        (self.nom, self.pv, self.niveau,self.xp, self.xp_niveau_suivant, self.attaque_min, self.attaque_max ,self.potions ),
        ("Bob", "bob@example.com", 25),
        ("Charlie", "charlie@example.com", 35),
        ]

        cursor.executemany(insert_query, users_data)

        conn.commit()
        conn.close()"""

    def utiliser_potion(self):
        """
        Permet au joueur d'utiliser une potion pour récupérer des PV.
        """
        if self.potions > 0:
            self.pv += 30
            self.potions -= 1
            print(f"{self.nom} utilise une potion et récupère 30 PV ! (Potions restantes : {self.potions})")
        else:
            print("Vous n'avez plus de potions !")

    def gagner_xp(self, xp_gagne):
        """
        Ajoute des points d'expérience et gère le niveau du joueur.
        """
        self.xp += xp_gagne
        print(f"{self.nom} gagne {xp_gagne} points d'expérience !")

        while self.xp >= self.xp_niveau_suivant:
            self.xp -= self.xp_niveau_suivant
            self.niveau += 1
            self.xp_niveau_suivant += 50
            self.pv += 20
            self.attaque_min += 2
            self.attaque_max += 3
            print(f"🎉 {self.nom} monte au niveau {self.niveau} !")
            print(f"Stats actuelles : PV = {self.pv}, Attaque = {self.attaque_min}-{self.attaque_max}")
