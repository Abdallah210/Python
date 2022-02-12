#coding:utf-8


#INTRODUCTION :

"""
Les structures séquentielles de données : sont des ensembles des élément (valeurs) de même type ou pas organisés séquentiellement 
auxquelles on peut accéder par leur numéro d'ordre (indice)


Les structures séquentielles vues jusqu'à maintenant :
1) Les chaînes de caractères (str) : 
    + contiennent que des caractères (?, !, A, a, B, b, C, c, ...)
    + non mutables : une fois définies on peut pas les modifier
    + itérable
    
2) Les listes (list) :
    + contiennent tout les types d'élément (str, list, bool, int, float, tuple ... )
    + mutables : on peut les modifier
    + itérable
 
3) Les tuples (tuple) :
    + contiennent tout les types d'élément (str, list, bool, int, float, tuple ... )
    + non mutables : une fois définies on peut pas les modifier
    + itérable

Les structures non séquentielles :
4) Les dictionnaires (dict) :
    + contiennent que les types non mutable (str, bool, int, float, ... )  #ne peut pas contenir des listes ou tuples
    + mutables : on peut les modifier
    + itérable

5) les ensembles : Les ensemble ou sets forment un autre type de données composites Python. Un ensemble est une collection
                   d'éléments non ordonnée, sans index et qui ne peut pas posséder l'élément dupliqué.
"""



#17 TUPLES

"""
Les tuples sont des structures séquentielles non mutables (comme les chaîne de caractère)


Les tuples disposent de deux méthodes (len et index):
        1 *Toutes les structures séquentielles disposent un indice à chaque élément qui la composes
        2 *Toutes les structures séquentielles on peut applique à eux la fonction len()

Il ne faut jamais oublier la virgule quand on veut créer un tuple :

tuple_1 = (5)   -->  int
tuple_1 = (5,)  -->  tuple



Création du tuple : nom_tuple = ()                  #tuple vide
                    nom_tuple = ("Hello !",)        #tuple avec une seule valeur
                    nom_tuple = 15,                 #tuple avec une seule valeur et sans parenthèses
                    nom_tuple = (12, "hello", ...)  #tuple avec plusieur valeurs

"""


# Les indices :

#                   0     1       2       3
premier_tuple = ("hello", 21, [1, 2, 3], True)

premier_tuple[0]   #'hello'
premier_tuple[1]   #21
premier_tuple[2]   #[1, 2, 3]
premier_tuple[3]   #True

#Fonction len() :

len(premier_tuple)  #4

"""
Construction d'un tuple par la fonction tuple() : il faut que l'objet qu'on veut transformer en tuple soit un itérable
un itérable est tous qu'on peut parcourir ces éléments (str, list ...)

"""
#Fonction tuple()
liste = ["Bonjour", 12, True]
chaine = "Aujourd'hui"

list_to_tuple = tuple(liste)
str_to_tuple = tuple(chaine)

print(list_to_tuple)  # ('Bonjour', 12, True)
print(str_to_tuple)   # ('A', 'u', 'j', 'o', 'u', 'r', 'd', "'", 'h', 'u', 'i')


"""
Opérations entre tuples :

concaténation :  "+"   tuple1 + tuple2

répétition : "*"  tuple1 * 3 

"""

#Concaténation :
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple1 + tuple2  #(1, 2, 3, 4, 5, 6)


#Répétition :
tuple1*3  #(1, 2, 3, 1, 2, 3, 1, 2, 3)


"""
Les tuples disposent des méthodes suivantes :
    tuple1.index(a) : renvoie l’indice du premier élément égal à a ;
    tuple2.count(a) : renvoie le nombre d’occurrence de a dans t

"""


tuple3 = ("hello",1,2,3,"hello",4,5,6,"hello")

#index = indice
tuple3.index(4)  #5
tuple3.index("hello")  #0  (avec cette méthode, Python prend la petite valeur de l'élément)

#count = combien de
tuple3.count("hello")  #3




"""
Une utilisation intéressante des tuples est l’affectation multiple:

Le nombre des variables doit être égal au nombre des élément du tuple 
"""

#Affectation multiple

nom_chiffre = ("zéro","un","deux","trois","quatre","cinq","six","sept","huit","neuf")

a,b,c,d,e,f,g,h,i,j = nom_chiffre 

print(a)  #zéro
print(b)  #un
print(c)  #deux
print(d)  #trois
print(e)  #quatre
print(f)  #cinq 
print(g)  #six
print(h)  #sept
print(i)  #huit
print(j)  #neuf




#Fonction qui renvoie un tuple :

def mon_divmod(a, b):
    """
    :param a: (int) un entier naturel
    :param b: (int) un entier naturel
    :return: (tuple) le couple (q, r) contenant le quotient et le
            reste de la division euclidienne de a par b
    :CU: a >= 0, b > 0
    :Exemples:
    >>> mon_divmod(0,1)
    (0, 0)
    >>> mon_divmod(26, 7)
    (3, 5)
    """
    q = 0
    r = a - b * q
    while r < 0 or r >= b:
        q = q + 1
        r = a - b * q
    return q, r


mon_divmod(26, 7)  #(3, 5)

#Affectation multiple par une fonction :
q, r = mon_divmod(26, 7)

print(q)  #3
print(r)  #5

