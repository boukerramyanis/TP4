from noeud import Noeud

n1 = Noeud(2, [])
n2 = Noeud("y", [])
n3 = Noeud("+", [])
n4 = Noeud("exp", [])

n3.ajouter_noeud(n1)
n3.ajouter_noeud(n2)
n4.ajouter_noeud(n3)

n3.affichage_polonais()