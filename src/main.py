from editeur import Editeur
from historique import Historique

# Test du Mémento avec ajout, enregistrement et restauration.

editeur = Editeur()
historique = Historique()

historique.Empiler(editeur.Sauvegarder())
editeur.Ecrire("Bonjour");
print("Texte: " + editeur.LireTexte())

historique.Empiler(editeur.Sauvegarder())
editeur.Ecrire(" le monde");
print("Texte: " + editeur.LireTexte())

historique.Empiler(editeur.Sauvegarder())
editeur.Ecrire(" !!!");
print("Texte: " + editeur.LireTexte())

print()
print("--- Annulations (undo) ---")

while (historique.EstVide() == False):
    print()
    print("Avant: [" + editeur.LireTexte() + "]")
    precedent = historique.Depiler()
    editeur.Restaurer(precedent)
    print("Après: [" + editeur.LireTexte() + "]")