class MementoEditeur:
    def __init__(self, texte):
        self.__texte = texte

    @property
    def texte(self):
        return self.__texte