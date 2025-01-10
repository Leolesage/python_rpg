import sqlite3


class Sauvegarde:
    def __init__(self, nom_bdd="sauvegarde.db"):
        self.nom_bdd = nom_bdd
        self.conn = sqlite3.connect(self.nom_bdd)
        self.creer_table()

    def creer_table(self):
        """Crée la table des sauvegardes si elle n'existe pas."""
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS joueurs (
                    nom TEXT PRIMARY KEY,
                    pv INTEGER,
                    niveau INTEGER,
                    xp INTEGER,
                    xp_niveau_suivant INTEGER,
                    attaque_min INTEGER,
                    attaque_max INTEGER,
                    potions INTEGER
                )
                """
            )

    def sauvegarder_joueur(self, joueur):
        """Sauvegarde les informations d'un joueur."""
        with self.conn:
            self.conn.execute(
                """
                INSERT OR REPLACE INTO joueurs (nom, pv, niveau, xp, xp_niveau_suivant, attaque_min, attaque_max, potions)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    joueur.nom,
                    joueur.pv,
                    joueur.niveau,
                    joueur.xp,
                    joueur.xp_niveau_suivant,
                    joueur.attaque_min,
                    joueur.attaque_max,
                    joueur.potions,
                ),
            )
        print(f"✅ Sauvegarde réussie pour le joueur {joueur.nom}.")

    def charger_joueur(self, nom):
        """Charge les informations d'un joueur à partir de la base de données."""
        with self.conn:
            curseur = self.conn.execute(
                "SELECT * FROM joueurs WHERE nom = ?", (nom,)
            )
            resultat = curseur.fetchone()

        if resultat:
            print(f"✅ Partie trouvée pour le joueur {nom}.")
            return {
                "nom": resultat[0],
                "pv": resultat[1],
                "niveau": resultat[2],
                "xp": resultat[3],
                "xp_niveau_suivant": resultat[4],
                "attaque_min": resultat[5],
                "attaque_max": resultat[6],
                "potions": resultat[7],
            }
        else:
            print(f"❌ Aucun joueur trouvé avec le nom {nom}.")
            return None

    def afficher_sauvegardes(self):
        """Affiche la liste des sauvegardes disponibles."""
        with self.conn:
            curseur = self.conn.execute("SELECT nom FROM joueurs")
            joueurs = curseur.fetchall()

        if joueurs:
            print("\n=== Sauvegardes disponibles ===")
            for joueur in joueurs:
                print(f"- {joueur[0]}")
        else:
            print("Aucune sauvegarde disponible.")

    def supprimer_sauvegarde(self, nom):
        """Supprime la sauvegarde d'un joueur."""
        with self.conn:
            self.conn.execute("DELETE FROM joueurs WHERE nom = ?", (nom,))
        print(f"✅ Sauvegarde de {nom} supprimée.")
