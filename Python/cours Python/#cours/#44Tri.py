# Effectuer un tri :



# I - La méthode sort() et la fonction sorted() :

"""
1 - Méthode sort() :
    + s'applique aux listes (liste numérique, liste de chaîne de caractères, liste des tuples)  

    + Syntaxe : liste.sort(key=None, reverse=False)
        - key et reverse = facultatifs                          

    + renvoie None mais elle modifie l'ordre de la liste

    + pour ranger les éléments à l'inverse : liste.sort(key=None, reverse=True)

"""


liste_int = [2, 1, 0, 3, 4]
liste_str = ["d", "a", "c", "b"]
liste_tuples = [(2, "D"), (5, "A"), (0, "B"), (1, "C")]

liste_int.sort()
liste_str.sort()
liste_tuples.sort()

liste_int     #[0, 1, 2, 3, 4]
liste_str     #['a', 'b', 'c', 'd']
liste_tuples  #[(0, 'B'), (1, 'C'), (2, 'D'), (5, 'A')]


liste_num2 =[3, 1, 2, 0]

liste_num2.sort(reverse=True)

liste_num2    #[3, 2, 1, 0]

"""
2 - Fonction sorted :
    + s'applique sur n'importe quel itérable

    + Syntaxe : sorted(itérable, key=None, reverse=False)
        - itérable : obligatoire
        - key et reverse : facultatifs

    + pour avoir un ordre inverse : sorted(itérable, reverse=True)

    + renvoie une liste avec les éléments de l'itérable rangés
"""

sorted('Abdallah')  #['A', 'a', 'a', 'b', 'd', 'h', 'l', 'l']

sorted('Abdallah', reverse=True)  #['l', 'l', 'h', 'd', 'b', 'a', 'a', 'A']



# II - Comparaison de deux valeurs :

"""
3 - Comparaisons de deux valeurs :
    + en général, on utilise les opérateurs mathématiques pour comparer des valeurs (<, >, = ...) 
    + en Python, on trouve des opérateurs prédifinies (==, =!, =>, > ...) 
    + les valeurs qu'on veut comparer doivent être de même type 
    + si on tente de comparer deux valeurs de types non comparables, une exception TypeError est déclenchée 
    
"""


#La fonction compare(), qu'on va définie, sert à comparer entre deux valeurs.
def compare(a, b):
    """
    les valeurs a et b doivent être de même type
    """
    if a < b :
        grande_valeur = b
        petite_valeur = a
        print("la valeur la plus grande est : {}\nla valeur la plus petite est : {}".format(grande_valeur, petite_valeur))
    elif b < a :
        grande_valeur = a
        petite_valeur = b
        print("la valeur la plus grande est : {}\nla valeur la plus petite est : {}".format(grande_valeur, petite_valeur))
    else :
        print('Les valeurs {} et {} sont égales'.format(str(a), str(b)))


"""
1 - Comparaison des nombres       : correspond à l'ordre numérique bien connu 

2 - Comparaison des booléens      : la booléen False est plus petite que la booléen True

3 - Comapraison des caractères    : l’ordre des caractères est déterminé par celui des numéros 
                                    Unicode (ASCII) associés

Exemple :
    + ord('T') == 84 et ord('a') == 97  donc ('T' <= 'a') == True

4 - Comparaison des chaîne        : correspond à l'ordre lexicographique (qui est la généralisation de l'ordre alphabétique)
  
5 - Comparaison des tuples        : correspond à l'ordre lexicographique mais il est nécessaire que les éléments 
                                    de mêmes rangs soient comparables.

6 - Comparaison des listes        : (comme les tuples)

En plus :
    + le tuple vide est inférieur à tous les autres tuples
    + la liste vide est inférieure à toutes les autres listes


7 - Comparaison des ensembles : Un ensemble e1 est «plus petit» qu’un ensemble e2 si le premier est un sous-ensemble 
                                du second.

En plus :
    + l’ensemble vide est donc le plus petit des ensembles.
    + on peut utiliser aussi la méthode issupset() pour comparaiser deux ensembles : ensemble1.issupset(ensemble2)

Avertissement : ___________________________________________________________________________________________________________
Contrairement aux nombres, chaînes de caractères, tuples, ce n’est pas parcequ’un ensemble n’est pas plus petit qu’un autre,
que l’autre est plus petit que le premier. En effet il est tout à fait possible pour deux ensembles qu’aucun des deux 
ne soit inclus dans l’autre.

Exemples :
>>> {0, 1, 2} <= {1, 2, 3}
False
>>> {1, 2, 3} <= {0, 1, 2}
False
___________________________________________________________________________________________________________________________


8 - Comparaison des dictionnaires : ce n'est pas possible 

dict() <= dict()
 ________________________________________________
| Traceback (most recent call last):             |
| ...                                            |
| TypeError: unorderable types: dict() <= dict() |
 ________________________________________________

"""


# 1 - Comparaison des nombres :
compare(5, 1.2)

"""
la valeur la plus grande est : 5
la valeur la plus petite est : 1.2
"""

# 2 - Comparaison des booléens :
compare(True, False)

"""
la valeur la plus grande est : True
la valeur la plus petite est : False
"""


# 3 - Comparaison des caratères :
compare('A','a')

"""
la valeur la plus grande est : a
la valeur la plus petite est : A
"""


# 4 - Comparaison des chaînes de caractères :
compare("Abdallah", "Elfilali")

"""
la valeur la plus grande est : Elfilali
la valeur la plus petite est : Abdallah
"""



# 5 - Comparaison des tuples :
compare((5,True,True),(5,True,False))

"""
la valeur la plus grande est : (5, True, True)
la valeur la plus petite est : (5, True, False)
"""

# 6 - Comparaison des listes :
compare([True,"a",(1,2,3,4) ],[True,"a",(1,2,3)])

"""
la valeur la plus grande est : [True, 'a', (1, 2, 3, 4)]
la valeur la plus petite est : [True, 'a', (1, 2, 3)]
"""

# 7 - Comparaison des ensembles (set) :
compare({0, 1, 2} , {0, 1, 2, 3})

"""
la valeur la plus grande est : {0, 1, 2, 3}
la valeur la plus petite est : {0, 1, 2}
"""

# 8 - Comparaison des dictionnaires : impossible




# III - Définir ses propres fonctions de comparaison :





classe = [('Timoleon', 13), ('Calbuth', 15), ('Talon', 12), ('Cru', 11)]


# première méthode : Fonction définie par moi

def compare_note(liste):
    liste_note_nom = []
    i = 0
    while i < len(liste):
        nouveau_tuple = (liste[i][1], liste[i][0]) 
        liste_note_nom.append(nouveau_tuple)
        i += 1
    liste_note_nom.sort(reverse=True)
    return liste_note_nom

print(compare_note(classe))





# deuxième méthode : importer la fonction cmp_to_key() et seq_compare_deuxieme()

import functools             #cmp_to_key()
import Modules_fst.compare   #seq_compare_deuxieme()

"""
seq_compare_deuxieme(x, y):
-->   -1 si x est plus petit que y ;
      0  si x est égal à y ;
      1  si x est plus grand que y.

"""

sorted(classe, key=functools.cmp_to_key(Modules_fst.compare.seq_compare_deuxieme))





#Troisième méthode : Création d'un fonction clé de notre choix

def premier(x):  
    return x[0]

def second(x):
    return x[1]

def troisieme(x):
    return x [2]

def quatrieme(x):
    return x [3]

def cinquieme(x):
    return x [4]

def sixieme(x):
    return x [5]
   
# l'ordre des notes : (math, physique, chimie, informatique)   

notes = [(12, 5, 18, 2), (15, 19, 18, 20), (5, 20, 4.5, 14)]

#math
sorted(notes, key=premier,reverse=True)    #[(15, 19, 18, 20), (12, 5, 18, 2), (5, 20, 4.5, 14)]

#physique
sorted(notes, key=second,reverse=True)     #[(5, 20, 4.5, 14), (15, 19, 18, 20), (12, 5, 18, 2)]

#chimie
sorted(notes, key=troisieme,reverse=True)  #[(12, 5, 18, 2), (15, 19, 18, 20), (5, 20, 4.5, 14)]

#informatique
sorted(notes, key=quatrieme,reverse=True)  #[(15, 19, 18, 20), (5, 20, 4.5, 14), (12, 5, 18, 2)]


#Quatrième méthode : la fonction lambda 

sorted(classe, key=lambda x :x[1], reverse=True)  #[('Calbuth', 15), ('Timoleon', 13), ('Talon', 12), ('Cru', 11)]





#IV - Tri par sélection :


# Selection du minimum :
def select_min(liste, a, b):
    """
    Renvoie l'indice du minimum de la tanche de la liste liste[a:n]
    Contarintes :
    - la liste doit être homogène
    - 0 =< a =< n =< len(liste)
    """
    indice_min = a
    i = a+1
    while i < b :
        if liste[indice_min] > liste[i]:
            indice_min = i
        i += 1 
    return indice_min

# Notion du coût :
"""
Déf : le coût == c(k)
c(k) est le nombre de comparaisons des éléments de la liste pour trouver le minimmum dans une tranche k = b-a (avec a<b)

"""

# Tri par sélection :

def tri_par_select(liste):
    """
    Renvoie la liste passée en paramètre rangée
    """
    i = 0
    n = len(liste)
    while i < n-1:
        indice_min = select_min(liste,i,n)
        liste.insert(i,liste[indice_min])
        del liste[indice_min+1]
        i+= 1
    return liste

tri_par_select(list("TIMOLEON"))  #['E', 'I', 'L', 'M', 'N', 'O', 'O', 'T']



