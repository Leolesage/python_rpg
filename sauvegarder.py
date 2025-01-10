import sqlite3
import os
import gameplay.personnages

class Sauvegarde:
    def __init__(self, db_path="sauvegarde.db"):
        """
        Initialise la classe Sauvegarde avec la connexion SQLite.
        :param db_path: Chemin vers la base de données SQLite.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.creer_table()

    def creer_table(self):
        """
        Crée la table pour sauvegarder les données si elle n'existe pas déjà.
        """
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS joueurs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    pv INTEGER NOT NULL,
                    niveau INTEGER NOT NULL,
                    xp INTEGER NOT NULL,
                    xp_niveau_suivant INTEGER NOT NULL,
                    attaque_min INTEGER NOT NULL,
                    attaque_max INTEGER NOT NULL,
                    potions INTEGER NOT NULL
                )
            """)

    def sauvegarder_joueur(self, joueur):
        """
        Sauvegarde les données d'un joueur dans la base de données.
        :param joueur: Objet du joueur à sauvegarder.
        """
        with self.conn:
            self.conn.execute("""
                INSERT INTO joueurs (nom, pv, mana, niveau, xp, xp_niveau_suivant, attaque_min, attaque_max, potions)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (joueur.nom, joueur.pv, joueur.niveau, joueur.xp, joueur.xp_niveau_suivant,
                  joueur.attaque_min, joueur.attaque_max, joueur.potions))
        print(f" La partie de {joueur.nom} a été sauvegardée avec succès.")

    def charger_joueur(self, nom):
        """
        Charge un joueur sauvegardé à partir de la base de données.
        :param nom: Nom du joueur à charger.
        :return: Un dictionnaire contenant les données du joueur ou None si le joueur n'existe pas.
        """
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM joueurs WHERE nom = ? ORDER BY id DESC LIMIT 1
            """, (nom,))
            data = cursor.fetchone()

        if data:
            print(f" Partie de {nom} chargée avec succès.")
            return {
                "nom": data[1],
                "pv": data[2],
                "niveau": data[3],
                "xp": data[4],
                "xp_niveau_suivant": data[5],
                "attaque_min": data[6],
                "attaque_max": data[7],
                "potions": data[8]
            }
        else:
            print(f" Aucun joueur trouvé avec le nom {nom}.")
            return None

    def afficher_sauvegardes(self):
        """
        Affiche toutes les sauvegardes disponibles.
        """
        with self.conn:
            cursor = self.conn.execute("SELECT nom, niveau FROM joueurs")
            sauvegardes = cursor.fetchall()

        if sauvegardes:
            print("\n=== Sauvegardes disponibles ===")
            for sauvegarde in sauvegardes:
                print(f"- {sauvegarde[0]} (Niveau {sauvegarde[1]})")
        else:
            print(" Aucune sauvegarde disponible.")

    def __del__(self):
        """
        Ferme la connexion à la base de données lorsque l'objet est supprimé.
        """
        self.conn.close()
