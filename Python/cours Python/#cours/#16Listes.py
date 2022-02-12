#Listes :

"""
listes homogènes : listes qui ont des éléments de même type

Exemples : 
liste des chaîne de caractères : ["abdallah","rachid","youssef","amine"]
liste des nombres              : [1, 5, 9, 4, 8]
liste des tuples               : [(1,), (True,5), ("bonjour", 5, False)]
"""


"""
1 - Syntaxe 
2 - Vocabullaire
    2.1 - les éléments 
    2.2 - les indices
3 - Manipulation
    3.1 - Preciser un élément ou plusieurs éléments de la liste
    3.2 - Les fonctions prédéfinies
    3.3 -


"""
#important  range(start, stop, step)

oiseaux = ["aigle", "flamant", "canard", "perroquet", "pigeon"]

oiseaux = ["aigle", "flamant", "canard", "perroquet", "pigeon"]

oiseaux = ["aigle", "flamant", "canard", "perroquet", "pigeon"]




#1 Syntaxe :

# liste standard   --->  nom_de_liste = [éléments]
# liste de nombres --->  nom_de_liste = range(a,b,c)     (a : nombre de départ  ; b : nombre d'arrivé exclus  ;  c : nombre de pas)


#2 Vocabulaire :

#2.1 les éléments :
# les éléments peuvent etre de n'importe type :

#                 bool      list      int    list     float    str    
liste_melangee = [True , [1 , 2 , 3] , 0 , range(10) , 2.1 , "neige" ]




#2.2 les indices (index en anglais) :

# chaque éléments de la liste à son indice et ces indices sont ordonnés de 0 jusqu'à n-1 (n nombres des élèments)

#                 0       1     2      3        4
liste_index = ["hiver" , 100 , 5.9 , False , "navire"] 



#3 Manipulation de la liste :

liste_str = ["matin" , "soir" , "nuit" , "journée" , "soirée"]



#3.1 Preciser un élément ou plusieurs éléments de la liste :

# ~ tout les éléments ~
#>>> print(liste_str[:])        
["matin" , "soir" , "nuit" , "journée" , "soirée"]



# ~ un seul élément ~
print(liste_str[0])        
#>>> "matin"
print(liste_str[1])        
#>>> "soir"
print(liste_str[2])        
#>>> "nuit"

print(liste_str[-1])       
#>>> "soirée"
print(liste_str[-2])       
#>>> "journée"
print(liste_str[-3])       
#>>> "nuit"



liste_str = ["matin" , "soir" , "nuit" , "journée" , "soirée"]


# ~ plusieurs éléments ~

print(liste_str[2:])       
#>>> ["nuit" , "journée" , "soirée"]  #indices 2,3 et 4

print(liste_str[1:4])      
#>>> ["soir" , "nuit" , "journée"]    #indices 1,2 et 3

print(liste_str[:3])       
#>>> ["matin" , "soir" , "nuit"]      #indices 0,1 et 2

"""
syntax :
liste_name[start:finish]

the index 'start' is included     ---> OK
the index 'finish' is excluded    ---> NO

liste_name[start:]  --> grabs from 'start' element to the ned 
liste_name[:finish] --> grabs from the first element to the 'finish' element 


"""


#------------
i = [0,1,2,3,4,5]
i[:3] # same as i[0:3] - grabs from first to third index (0->2)
[0, 1, 2]
i[3:] # same as i[3:len(i)] - grabs from fourth index to end
[3, 4, 5]






#3.2 Les méthodes des listes :

"""
___________________________________________________________________________

1) Append --> Append object to the end of the list.

Syntax : list.append(element)

*append == add to the very end
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

>>> print(fruits)  
["apple", "banana", "cherry", "orange"]
____________________________________________________________________________



____________________________________________________________________________

2) Clear --> Remove all items from list. 

Syntax : list.clear()
     
*clear ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

>>> print(fruits)  
[]
____________________________________________________________________________



____________________________________________________________________________

3) Copy --> Return a shallow copy of the list.

Syntax : list.copy()

*copy == 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

>>> print(x)
['apple', 'banana', 'cherry', 'orange']
____________________________________________________________________________



____________________________________________________________________________

4) Count --> Return number of occurrences of value.

Syntax : list.count(element)

* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :
fruits = ['cherry', 'apple', 'banana', 'cherry']
x = fruits.count("cherry")

>>> print(x)  
2
____________________________________________________________________________


____________________________________________________________________________

5) Extend --> Extend list by appending elements from the iterable.

Syntax :  
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :
  extend(self, iterable, /)
      Extend list by appending elements from the iterable.

>>> print()  

____________________________________________________________________________



____________________________________________________________________________

6)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________



____________________________________________________________________________

7)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________



____________________________________________________________________________

8)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________



____________________________________________________________________________

9)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________



____________________________________________________________________________

10)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________



____________________________________________________________________________

11)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________



____________________________________________________________________________

12)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________



____________________________________________________________________________

13)  -->  

Syntax : 
     
* ==
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

#Exemple :


>>> print()  

____________________________________________________________________________













 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.




 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |    
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.

"""









































