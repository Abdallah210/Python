#coding:utf-8

"""
Syntaxe : assert <condition> , <optional message>

La condition doit être vrai.

Le message optionnel s'affiche quand la condition n'est pas respectée.
"""

#Example :

def voy_con(lettre):
    assert len(lettre) == 1, "il faut insérer au moins une lettre" 
    if lettre in list("aeiouy"):
        print("La lettre insérée est une voyelle !")
    else :
        print("La lettre insérée est une consonne !")


#voy_con("a")     --> La lettre insérée est une voyelle !
#voy_con("z")     --> La lettre insérée est une consonne !
#voy_con("")     --> AssertionError: il faut insérer une seule lettre
#voy_con("qsd")  --> AssertionError: il faut insérer une seule lettre


#Exemple 2 :

x = False
assert x == True, "x doit être True" # AssertionError
