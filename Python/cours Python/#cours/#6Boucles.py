#coding:utf-8

#6 BOUCLES :


# Répétition de la phrase 5 fois :
print("Répétition sans boucle : 5 lignes écrites ")
print("je suis une phrase ")
print("je suis une phrase ")
print("je suis une phrase ")
print("je suis une phrase ")
print("je suis une phrase ")



"""
Pour éviter de répéter la phrase, on utilisera la boucle for ou while :

Boucles : while (puisque)
          for ... in (pour ... dans)


Les boucles fonctionnent avec des variables et les opérateurs de comparaison (comme les conditions)

Mots-clés : break (casser la boucle)
            continue (revenir au début de la boucle)  
"""


#Boucle while :
print("\n\nRépétition avec bouble while : 4 lignes écrites")

compteur = 0
while compteur < 5 :
    print("je suis une phrase ")
    compteur += 1  #incrémentation du compteur


#Boucle for  :
print("\n\nRépétition avec bouble for : 3 lignes écrites")

rep = "12345" #chaîne de 5 caractères
for x in rep :
    print("je suis une phrase ") 

print("\n\nRépétition avec bouble for : 1 ligne écrite (optimisé le 29/10/2021)")

for x in range(5) : print("je suis une phrase ") 




# Utilisation du mot-clé "break" :
print("\n\nUtilisation du mot-clé break : ")


#Avec while :  _____________________________________________________________________
print("\nAvec la boucle while :")

#Exemple 1 :
print("\nExepmle 1 :")

fruits = ["pomme", "pêche", "melon", "cerise", "poire", "abricot"]

i = 0
while i < 100 :
    if len(fruits) == 2 :
        break 
    del fruits[0]
    print(i, fruits)
    i += 1

#Exemple 2 :
print("\nExepmle 2 :")

while True :
    nombre = float(input("insérer un nombre positif : "))
    if nombre < 0 :
        print("Error : le nombre inséré est incorrect .")
        break
    else :
        print("Vous avez inséré", nombre, "!")

#____________________________________________________________________________________


#Avec for :  _________________________________________________________________________
print("\nAvec la boucle for :")

phrase = "je m'appelle Abdellah, et j'ai 21 ans . "
nouvelle_phrase = ""
for caractere in phrase :
    if caractere == "," :
        break
    nouvelle_phrase += caractere  
    print(nouvelle_phrase)

#______________________________________________________________________________________



# Utilisation du mot-clé "continue" :
print("\n\nUtilisation du mot-clé continue : ")


#Avec la boucle while :__________________________________________________________________
print("\nAvec la boucle for :")

i = 0
titre = "Attack on titan"
nouveau_titre = ""
ligne = 0
while i < len(titre) :
    if titre[i] == " " :
        i += 1
        continue 
    nouveau_titre += titre[i] 
    ligne += 1
    print(ligne, " ", nouveau_titre)
    i += 1
#_________________________________________________________________________________________
 


#Avec la boucle for :  __________________________________________________________________
print("\nAvec la boucle for :")

i = 0
j = 0
for x in range(5):  # le range(n) on peut le considéré comme : "n fois" 
    nombre = float(input("insérez un nombre positif :"))
    if nombre < 0 :
        print("le nombre", nombre, "est négatif !")
        continue 
    elif nombre == 0.0 :
        print("le nombre", nombre, "est nul !")    
        j += 1
        continue  
    print("le nombre", nombre, "est positif !")
    i += 1
print("les nombres positifs insérés sont :", i)
print("les nombres négatifs insérés sont :", 5-(i+j))
print("les nombres nuls insérés sont :", j)

#______________________________________________________________________________________



"""
#1 Boucle While :
Pour la boucle while il faut créer une variable (compteur) pour l'arrêter 

Le point d'arrêt est le point où la boucle s'arrêtera 
En langage de programmation, on appelle le point d'arrêt i (j, k, l ... (s'il y a plusieur boucles ))

Pour arriver au un point d'arrêt : on incrémente la variable i par la valeur qu'on veut (généralement par 1)

A différence de boucle for, la boucle while ne nécessite pas un itérable pour fonctionner.

""" 

###     [while (while ~ while)]




"""
#2 Boucle for :

La boucle for permet la répétition d’un bloc d’instructions sur chacune des valeurs d’un itérable.


Un itérable est une séquence de valeurs que l’on va pouvoir parcourir.

Les itérables : str (chaîne de caractère)
                range (intervalle)
                list (liste)
                tuple (tuple)
                dict (dictionnaire)
                set (???)

"""


#Boucle for avec une chaîne de caractère :
print("\n\nBoucle for avec str :")

mot = "giraffe"
mot_inverse = ""
mot_non_inverse = ""
compteur = -1
for lettre in mot :
    mot_non_inverse += lettre 
    mot_inverse = lettre + mot_inverse   #Pour inverser le mot
    compteur += 1   #Pour afficher l'indice du caractère dans la chaîne
    print(compteur, " ", lettre, " ", mot_non_inverse, " ", mot_inverse)




#Boucle for avec un intervalle :
print("\n\nBoucle for avec range :")

liste_nombres = []
fact = 1 
for nombre in range(5):
    liste_nombres.append(nombre)  #créer une liste des nombres
    f = nombre + 1
    fact *= f  #pour calcule le factoriel (seulement si range contient un seul paramètre)
    print(nombre, " ", liste_nombres, " ", fact)




#Boucle for avec une liste :
print("\n\nBoucle for avec list :")

liste_animaux = ["cheval", "chévre", "vache", "mouton", "chien", "chat", "souris", "giraffe", "éléphant", "lion"]
vider_liste = liste_animaux.copy()  #cloner liste_animaux
for animaux in  liste_animaux :
    del vider_liste[0]   #pour vider la liste créée
    print(liste_animaux.index(animaux), " ", animaux, " ", vider_liste)




#Boucle for avec un tuple :
print("\n\nBoucle for avec tuple :")




#Boucle for avec un dictionnaire :
print("\n\nBoucle for avec dict :")




#Boucle for avec un set :
print("\n\nBoucle for avec set :")


























