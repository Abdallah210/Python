#coding:utf-8

#3 Variables 

"""
Nommer une variable : doit commencer par une lettre ou un underscore
                      ne pas contenir des caractères spéciaux
                      ne pas contenir d'espaces 
                      utiliser des underscore (_)
"""

agePersonne = 0   #Camel Case
Age_Personne = 0  #Camel Case
age_personne = 0
agepersonne = 0
_agepersonne = 0

"""
Dans des projets il faut adobter toujours la même syntaxe des variables pour avoir des variables homogènes 


_________ Exemple 1 : ____________
NomJoueur = ...
Prenom_joueur = ...
age_joueur = ...
__________________________________

_________ Exemple 2 : ____________
nom_joueur = ...
prenom_joueur = ...
age_joueur = ...
__________________________________

** Le premier exemple à eviter !!! **

"""

#Pour affecter une valeur à une variable, on utilise un égal (=) entre eux 

salutation = "Bonjour !"  #affectation



"""
Type de données : entier (int)
                  nombre flottant (float)
                  chaîne de caractère (str)
                  booléen (bool)
                  liste (list)
                  tuple (tuple)
                  dictionnaire (dict)
                  ensemble (set)
                  ...

les ensembles : Les ensemble ou sets forment un autre type de données composites Python. Un ensemble est une collection
                d'éléments non ordonnée, sans index et qui ne peut pas posséder l'élément dupliqué.

All data types built-in by default :
___________________________________________________
Text Type  	       |             str              |
___________________________________________________
Numeric Types 	   |      int, float, complex     |
___________________________________________________
Sequence Types     |      list, tuple, range      |
___________________________________________________
Mapping Type 	   |             dict             |
___________________________________________________
Set Types 	       |        set, frozenset        |
___________________________________________________
Boolean Type       |             bool             |
___________________________________________________
Binary Types       | bytes, bytearray, memoryview |
___________________________________________________

 
type () --> est une fonction qui retourne tout simplement le type d'une donnée  

"""
#Type d'une donnée :
print("Type d'une donnée :\n")

print(type("Hello !"))    #str
print(type(6.0))          #float
print(type(False), "\n")  #bool


"""
Pour afficher une variable, on utilise la fonction print()
*Dans da la fonction print(), la virgule est se remplace avec un espace à la sortie des données

"""

# Affichage de la variable :
print("Affichage de la variable :\n")

x = "Bonjour !"

print(x)  # Bonjour !

nom = "Elfilali"
prenom = "Abdallah"

print(nom , prenom)  # Elfilali Abdallah

print("Bonjour " , nom , " " , prenom , " !")  # Bonjour Elfilali Abdallah !




# la fonction format() :
print("\n Affichage de la variable avec la fonction format :\n")

#méthode 1
phrase = "mon nom complet est : {} {} ."
print(phrase.format(nom , prenom))  # mon nom complet est : Elfilali Abdallah .

#méthode 2
print("mon nom complet est : {} {} .".format(nom , prenom))  # mon nom complet est : Elfilali Abdallah .


#Convertir la donnée : ( fonction type() )
print("\nConvertir la donnée :\n")

print(bool(0))            # False
print(bool(1))            # True
print(int("125"))         # 125
print(str(55))            # "55"
print(list("Bonjour !"))  # ["B", "o", "n", "j", "o", "u", "r", " ", "!"]

#valable aussi :
nom = "Elfilali"
print(list(nom))   #["E", "l", "f", "i", "l", "a", "l", "i"]

"""
Fonctions vues : 
    print()       -> afficher sur l'ecran
    input()       -> lire au clavier
    type()        -> retourne le type d'une donnée
    str.format()  -> formater une chaîne de caractère
    int(), float(), str(), list()...   -> "caster" une donnée (la convertir)
                 
"""


#4 Les opérateurs :

print("\nLes opérateurs : \n")
"""
Les opérateurs Python : +  (addition)
                        -  (sutraction)
                        *  (multiplication)
                        /  (division euclidienne) 
                        // (quotient de la division)
                        %  (modulo ou reste du la division)


Syntaxe raccourci :
variable = variable + x
variable += x

variable = variable * x
variable *= x

variable = variable - x
variable -= x

...

"""
print(11 + 3)   #14 
print(11 - 3)   #8
print(11 * 3)   #33
print(11 / 3)   #3.66666666
print(11 // 3)  #3
print(11 % 3)   #2



















