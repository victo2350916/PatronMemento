from mementoEditeur import MementoEditeur

# Objet pour lequel on veut sauvegarder l'état
class Editeur:
    def __init__(self):
        self.__texte = ""

    # Ajoute du texte à celui déjà présent
    def Ecrire(self, ajout):
        self.__texte = self.__texte + ajout

    # Retroune le texte
    def LireTexte(self):
        return self.__texte

    # Sauvegarde l'état du texte dans un Mémento
    def Sauvegarder(self) -> MementoEditeur:
        return MementoEditeur(self.__texte)

    # Restaure l'état à partir d'un Mémento
    def Restaurer(self, memento: MementoEditeur):
        if memento is None:
            return
        self.__texte = memento.texte