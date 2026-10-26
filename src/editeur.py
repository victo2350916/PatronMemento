from mementoEditeur import MementoEditeur

class Editeur:
    def __init__(self):
        self.__texte = ""

    def Ecrire(self, ajout):
        self.__texte = self.__texte + ajout

    def LireTexte(self):
        return self.__texte

    def Sauvegarder(self) -> MementoEditeur:
        return MementoEditeur(self.__texte)

    def Restaurer(self, memento: MementoEditeur):
        if memento is None:
            return
        self.__texte = memento.texte