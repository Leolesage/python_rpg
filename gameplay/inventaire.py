class Inventaire:
    def __init__(self):
        self.objets = []

    def ajouter_objet(self, objet):
        """Ajoute un objet à l'inventaire."""
        self.objets.append(objet)
        print(f"Vous avez ajouté {objet} à votre inventaire.")

    def afficher(self):
        """Affiche le contenu de l'inventaire."""
        if not self.objets:
            print("Votre inventaire est vide.")
        else:
            print("Inventaire :")
            for objet in self.objets:
                print(f"- {objet}")
