#coding:utf-8

#7 FONCTION :

"""
Différent noms des fonctions : la fonction  --> Renvoie des valeurs quelconques
                               le prédicat  --> Renvoie toujours une valeur booléen (True or False)
                               la procédure --> Ne renvoie rien seulement affiche des infos

"""


"""
Il y a deux types de fonctions : fonction prédéfinie (déjà existants dans le langage Python)
                                 fonctions définies par nous

Quelques fonctions déjà définie par Python :  print()
                                              input()
                                              len()
                                              int(), float(), str(), bool(), list()...
                                              min() et max()
                                              range()
                                              abs()
                                              all() et any()
                                              type()
                                              ord()
                                              chr()
                                              ... (voir le script '#9997 fonctions prédéfinies' pour voir des autres fonctions)  
                                              

Nommer une fonction : doit commencer par une lettre ou un underscore
                      ne pas contenir des caractères spéciaux 
                      ne pas contenir d'espaces 
                      utiliser des underscore (_)
                      (Même nommage d'une variable)
                      + ne pas la nommer par un nom résérvé à une fonction prédéfinie par Python


Définir une fonction : commener par 'def' puis nommer la fonction.

La fonction peut prendre plusieur paramètres 

Il faut réspecter l'identation après le nommage de la fonction et une fois on la réspecte pas on sortit de la fonction 

"""

# Exemple 1 :
def carré(x):     # x est un paramètre
    carre = x**2
    return carre    # renvoie le carré du nombre passé en paramètre

carré(4)          # la valeur 16 ne s'affiche pas  au terminal 
print(carré(4))   # la valeur 16 s'afficher au terminal

"""
La fonction peut rester sans paramètre (Exemple 2) 
"""
#Fonction sans paramètre :
print("Fonction sans paramètre :")

# Exemple 2 :
def message():
    print("Hello hello my name is Zrereq !")

message()  # affichage du message dans le terminal   


#Plusieurs paramètres :
print("\n\nPlusieurs paramètres :")

# Exemple 3 : (dialogue)

def dire(nom_personne , message):
    print("{} : {} ".format(nom_personne,message))

"""
return : renvoyer quelque chose par l'appelle à la fonction.  

L'appelle à la fonction se fait sans le mot 'def' avec les paramètres voulus

"""

#Appelle de la fonction de l'exemple 2 :
dire("Abdallah", "Bonjour à tout le monde !") 
dire("Tout","Bonjour Monsieur Abdallah !") 

"""
Dans la définition de la fonction, on peut choisir des valeurs des paramètres par défaut (exemple 4) 
"""

#Paramètres par défaut :
print("\n\nParamètres par défaut :")

# Exemple 4 :
def repeat(n=3):
    for x in range(n):
        print("cette ligne est la ligne numèro : {}.".format(str(x+1))) 
    

repeat(5)  #avec 5 en paramètre
"""
au terminal -->  | cette ligne est la ligne numèro : 1.
                 | cette ligne est la ligne numèro : 2.
                 | cette ligne est la ligne numèro : 3.
                 | cette ligne est la ligne numèro : 4.
                 | cette ligne est la ligne numèro : 5.
"""

print("")

repeat()  #sans paramètre 
"""
au terminal -->  | cette ligne est la ligne numèro : 1.
                 | cette ligne est la ligne numèro : 2.
                 | cette ligne est la ligne numèro : 3.
"""



"""
Pendant l'applle à la fonction, Python suit l'ordre des paramètres mais on peut préciser chaque valeur pour chaque paramètre (exemples 5, 6 et 7)

"""

#Ordre des paramètres :
print("\n\nOrdre des paramètres :")
def félicitaion(nom, anniv):
    print("Cher {}, nous vous félicitons pour ton {}ème anniversaire !".format(nom,str(anniv)))


# Exemple 5 :
               #1      #2
félicitaion("Abdallah",21)
"""
au terminal -->  | Cher Abdallah, nous vous félicitons pour ton 21ème anniversaire !

"""

# Exemple 6 :
            #1     #2
félicitaion(21,"Abdallah") #les paramètres sont mal ordonnés
"""
au terminal -->  | Cher 21, nous vous félicitons pour ton Abdallahème anniversaire ! 

"""

# Exemple 7 :
               #2         #1
félicitaion(anniv=21,nom="Abdallah") #les paramètres sont bien ordonnés
"""
au terminal -->  | Cher Abdallah, nous vous félicitons pour ton 21ème anniversaire !

"""


"""
Pour que la fonction prend une infinité des paramètres il faut mettre une étoile '*' juste avant le nom 
du paramètre (exemple 8) 


"""

#Une infinitée des paramètres :
print("\n\nUne infinité des paramètres :\n")


# Exemple 8 :
def participants(*nom_joueurs):
    i = 0
    for joueur in nom_joueurs :
        i += 1
        if i == 1:
            print("Le " + str(i) + "er joueur est {}.".format(joueur))
        else :
            print("Le " + str(i) + "ème joueur est {}.".format(joueur))


participants("Abdellah", "Rachid", "Youssef", "Yassin", "Ayman", "Mohammed")

"""
au terminal -->  | Le 1er joueur est Abdallah. 
                 | Le 2ème joueur est Rachid.
                 | Le 3ème joueur est Youssef.
                 | Le 4ème joueur est Yassin.
                 | Le 5ème joueur est Ayman.
                 | Le 6ème joueur est Mohammed
"""


#la fonction lambda
"""
la fontion lambda est une fonction sans nom et pour l'appeler il faut l'affecter à une variable. (exemple 9)

A quoi sert ?
tout simplement sert renvoyer une fonction avec une seule instruction
"""
# Exemple 9 : (sans paramètre)

coucou = lambda: print("Bonjour !")
coucou()  #il va s'affiche 'Bonjour !' dans le terminal



# Exemple 10 : (avec un paramètre)
"""
ttc : toutes taxes comprises
prix ht : prix hors taxes
tva : taux de la taxes sur la valeur ajoutée
"""
ttc = lambda prixht : prixht + (prixht * (20 / 100 ))
ttc(80)  #96.0



# Exemple 11 : (avec deux paramètres)

somme = lambda nombre1, nombre2 : nombre1 + nombre2
somme(2,3)  #5


"""
Si on affecte une nouvelle valeur à la variable de la fonction lambda, cette dérnière ne fonctionnera pas (exemple 12)
"""

# Exemple 12 :

rire = lambda rire : print("{} comme vous êtes drôle !".format(rire))
rire("Hahahahaha")

rire = "Hihiihi" 

# rire("Hehehehe")   --> TypeError
