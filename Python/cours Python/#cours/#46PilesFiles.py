# Piles :

"""
Sont-ils quoi les piles ?

Les piles sont des structures de données linéaires. 

______________________________________________________________________
| Les piles peuvent contenir en principe autant d’éléments qu’on     |
| veut (cependant en réalité elles sont en général limitées par      |
| la mémoire disponible). Mais il n’est pas possible d’accéder       |
| directement à n’importe lequel de ces éléments : seul l’élément    | 
| qui y a été placé en dernier est accessible, les autres ne l’étant | 
| pas tant que ce dernier élément n’a pas été sorti de la pile.      |
| C’est le principe du dernier entré, premier sorti ou               |
| Last In First Out (LIFO en abrégé)                                 |
______________________________________________________________________



Structure de données importante en informatique :

    1 - pile des appels de fonctions

    2 - utile pour parcours de graphes (trouver un chemin)

    3 - exemple de l’évaluation d’expressions postfixées

"""

# Opérations primitives sur les piles :

"""
Les opérations primitives que les piles admettent sont :

    1 - Constructeur --> création d’une pile  

    2 - Sélecteur    --> empilement d’un élément sur une pile ;

    3 - Modificateur --> dépilement d’une pile ;

    4 - Modificateur --> consultation du sommet d’une pile ;

    5 - Prédicat     --> test de vacuité d’une pile.

"""

# 1 - Constructeur :

def stack():
    """
    Crée un pile vide (liste)
    Paramètres : None
    Valeur de retour : list
    Contraintes : None
    Exemple :
    >>> pile = stack()
    >>> pile == []
    True
    """
    return list()


# 2 - Sélecteur :

def empiler(pile, element):
    """
    Ajout d'element 'element' dans la pile passée en paramètre
    Paramètres : 
    - pile    : list, une pile
    - element : any, l'élément à ajouté
    Valeur de retour : None
    Contraintes : None
    Exemple :
    >>> pile = stack()
    >>> empiler(pile, 2)
    >>> pile == [2]
    True
    """
    pile.append(element)


def depiler(pile):
    """
    Renvoie le dernier élément ajouté dasn la pile
    Paramètres : 
    - pile    : list, une pile à modifiée
    Valeur de retour : any (type d'élément)
    Contraintes : 
    - pile != []
    Exemple :
    >>> pile = stack()
    >>> empiler(pile, 2)
    >>> empiler(pile, 3)
    >>> pile == [2, 3]
    >>> depiler(pile)
    3
    """
    return pile.pop()
