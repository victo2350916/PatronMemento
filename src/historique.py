from mementoEditeur import MementoEditeur

# Historique des Mémento
class Historique:
    def __init__(self):
        self.__pile = []

    # Ajoute un Mémento à la pile
    def Empiler(self, memento: MementoEditeur):
        self.__pile.append(memento)

    # Retourne le premier Mémento de la pile et le supprime de celle-ci
    def Depiler(self) -> MementoEditeur:
        if  len(self.__pile) == 0:
            return None
        return self.__pile.pop()

    # Vérifie si la pile de Mémento est vide
    def EstVide(self):
        if len(self.__pile) == 0:
            return True
        else:
            return False
