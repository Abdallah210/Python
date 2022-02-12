#coding:utf-8 

#INTRODUCTION :
"""
Les structures séquentielles itérables : chaîne de caractères (str)
                                         liste (list)
                                         range (range)
                                         tuple (tuple)

Les structures séquentielles non itérables : dictionnaire (dict)

"""


#18 DICTIONNAIRES :

"""
Les dictionnaires sont des structures de données permettant d’associer une valeur à une clé.


Dans un dictionnaire, il ne peut y avoir qu’une seule association pour une clé donnée. 
Dit autrement, dans un dictionnaire les clés sont uniques.


Syntaxe : 
méthode 1: syntaxe normale
nom_dict = {cle1 : valeur1, cle2 : valeur2, ...}

méthode 2 :Par la fonction dict() + une liste des tuples
tarifs = dict([(clé1, valeur1), (clé2, valeur2), (clé3, valeur3)])

"""

#méthode 1 :
couleurs = { "rouge" : "feu", "vert" : "erbre", "marron" : "terre", "bleu" : "eau" }

#méthode 2
tarifs = dict([('banane', 2.59), ('pomme',1.95), ('orange',1.95)])



couleurs  #{ "rouge" : "feu", "vert" : "erbre", "marron" : "terre", "bleu" : "eau" }

#accéder à la valeur à travers la clé (l'inverse n'est pas possible) :
couleurs["bleu"]  #eau
couleurs["rouge"]  #feu
couleurs["marron"]  #terre
couleurs["vert"]  #erbre



"""
Seules les valeurs non mutables peuvent servir de clé dans une association.
c-à-d on peut pas utiliser les listes, les dictionnaires ... comme clé d'un dictionnaire

"""
dict_vide = {} #dictionnaire vide
dict_vide = dict() #dictionnaire vide


dict_vide  #{}
dict() #{}



"""
On peut utiliser la fonction len()pour calculer la langeur du dictionnaire


"""
#Taille d’un dictionnaire

tarifs = {'banane':2.59, 'pomme':1.95, 'orange':1.95}

len(tarifs) #3


"""
1) Recherche
Existence d’une association pour une clé donnée (Exemple 1)
    clé in nom_dict --> True or False


2) Modification (Ajout)
Les dictionnaires sont des structures mutables.On peut modifier la valeur associée à une clé (Exemple 2)
    nom_dict[clé] = nouvelle_valeur


3) Modification (Change)
On peut aussi modifier un dictionnaire en ajoutant une association. (Exemple 3)
    nom_dict[nouvelle_clé] = nouvelle_valeur
    

4) Modification (Suppression)
On peut enfin supprimer une association dans un dictionnaire. (Exemple 4)
    On le fait avec l’instruction del.
    del nom_dict[clé_à_supprimée]

"""

cotes = {"cercle": "inf", "triangle": 3, "carré": 4,"pentagone": 5, "hexagone": 6 , "octagone": 8}

#Exemple 1 : 

"cercle" in cotes  #True
"trapezoide" in cotes  #False


#Exemple 2 : 

cotes["cercle"] = 0
cotes["cercle"]  #0


#Exemple 3 : 

cotes["trapezoide"] = 4
cotes["trapezoide"]  #4
cotes #{"cercle": "inf","triangle": 3, "carré": 4,"pentagone": 5, "hexagone": 6 , "octagone": 8, "trapezoide": 4}



#Exemple 4 : 

del cotes["cercle"]
cotes #{"triangle": 3, "carré": 4,"pentagone": 5, "hexagone": 6 , "octagone": 8, "trapezoide": 4}



#Itération :
"""
Attention !!!

Les dictionnaires ne sont pas des structures séquentielles. 
Il n’est donc pas possible dans un traitement itératif des données contenues dans un 
dictionnaire de s’appuyer sur un quelconque ordre de ces données.

C-à-d on peut pas itérer le dictionnaire par un ordre comme montre l'exemple suivant :

for x in range(5) :        
    print(cotes[x])         #FAUX

"""


for cle in cotes :
    print(cle)

#triangle
#carré
#pentagone
#hexagone
#octagone
#trapezoide



for cle in cotes :
    print(cotes[cle])

#3
#4
#5
#6
#8
#4
