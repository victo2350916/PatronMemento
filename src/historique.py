from mementoEditeur import MementoEditeur

class Historique:
    def __init__(self):
        self.__pile = []

    def Empiler(self, memento: MementoEditeur):
        self.__pile.append(memento)

    def Depiler(self) -> MementoEditeur:
        if  len(self.__pile) == 0:
            return None
        return self.__pile.pop()

    def EstVide(self):
        if len(self.__pile) == 0:
            return True
        else:
            return False
