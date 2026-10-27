# Mémento dans lequel l'état est stocké
class MementoEditeur:
    def __init__(self, texte):
        self.__texte = texte

    # Propriété en lecture seul
    @property
    def texte(self):
        return self.__texte