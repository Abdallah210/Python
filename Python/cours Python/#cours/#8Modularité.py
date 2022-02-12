#coding:utf-8

"""
La modularité indique qu'on va faire intervenir des modules (bibliothéques), ces modules contiennent des fonctios prédéfinies

Si on utilise une fonction d'un module et on exécute le programme sans importer ce module, il affichera un Error (function not defined) 

Un module plus exactement est un fichier

Syntaxe : NomModule.FonctionModule()  --> si on import tout le module (exemple 1.1)
          FonctionModule()  --> si on importe uniquement la fonction ou toutes les fonctions du module  (exemples 1.2 et 1.3)

Importer un module : import <NomModule> 
                     from <NomModule> import <NomFonction>
                     from <NomModule> import *

les modules sert dans des domaines plus précis (exemple 1)
"""

# Exemple 1 : Calculer quelque chose plus avancé en mathématique 
print("Module du math :")


# Exemple 1.1 :
import math   #importer tout le module  

racine = math.sqrt(25)
print(racine)  #5.0


# Exemple 1.2 :
from math import sqrt   #importer une seule fonction 

racine = sqrt(100)
print(racine) #10.0


# Exemple 1.3 :
from math import sin   # '*' pour importer toutes les fonctions 

sinus = sin(0) 
print(sinus)  #0.0

"""
Quelque modules : doctest
                  random
                  math
                  cmath
                  os
                  functools
                  pickle
                  statistics
                  requests
                  ...
                  
"""

"""
Créer un fichier (module) : 1) créer un nouveau fichier '.py'
                            2) importer le fichier (module) créé


Importer un fichier : 
 + Si le fichier se trouve dans le même dossier du fichier principale : import <NomFichier> 
                                                                        from <NomFichier> import <NomFonction>
                                                                        from <NomFichier> import *

 + Si le fichier se trouve dans un autre dossier : import <NomDossier>.<NomFichier> 
                                                   from <NomDossier>.<NomFichier> import <NomFonction>
                                                   from <NomDossier>.<NomFichier> import *
 
 + Si on utilise uniquement import : il faut écrire le nom du fichier et le dossier où se trouve avant chaque fonction pour l'appeler 
                                     Pour eviter d'écrire tout le nom, on peut utiliser le mot-clé 'as' (exemple 3)
                                     Syntaxe : import <NomDossier1>.<NomDossier2>.<NomFichier> as <NomdeChoix>

PyCache :
Quand on importe un fichier automatiquement il  va se créer un dossier où se trouve le fichier appelé "__pycache__"  

Le dossier "__pycache__" est un répértoir de cache pour Python

Dans autres langage il faut créer ce dossier manuellement



"""

# Exemple 2 :

from Modules.dialogue import message
from Modules.dialogue import parler
from Modules.dialogue import nom
from Modules.dialogue import choix
from Modules.dialogue import cliquer
from Modules.dialogue import Salutation

message("Tu reveilles dans un laboratoire")
cliquer()
parler(message=Salutation(Ajout=" Finalement t'es reveillé !"))
cliquer()
parler("Toi",)
cliquer()
parler(message="Tu est encore sous l'effet du shock .")
cliquer()
parler(message="T'inquiéte pas, je vais t'éxpliquer tout !")
cliquer()
parler("Dr.Abdallah","Mon nom est Dr.Abdallah .")
cliquer()
parler("Dr.Abdallah","Est-ce tu rappeles de ton nom ?")
cliquer()
parler("Toi","Oui")
NomJoueur = nom()
parler("Dr.Abdallah","Super ! Alors ton nom est {} ?".format(NomJoueur))
cliquer()
parler("Toi",message=choix())
parler("Dr.Abdallah", "Magnifique ! ")
cliquer()
parler("Toi", "Que ce je fait ici ?")
cliquer()


# Exemple 3 :

import Modules.rire as drôle

parler("Dr.Abdallah",message=drôle.rire())  #au lieu de : parler("Dr.Abdallah",message=Modules.rire.rire())


"""
Documenter une fonction : la documentation se fait sous forme d'un commentaire (de ligne 2 jusqu'à la ligne 14 de l'exemple 4
                          la documentation contient plusieurs infos sur la fonction (Sa fonction,Paramètres,Valeur de retour,Contraintes,Exemples...) 
                          la documentation doit réspester l'identation
                          les exemples sont des docstrings grâce à eux on peut savoir si la fonction fonctionner correctement ou pas
                          les docstrings sont les lignes 12 et 13 de l'exemple 4 (l'exemple sous forme de commentaire)  
                          les docstrings s'éffectuent à l'aide du module doctest (exemple 5)


Exemple 4 : 
1  | def fonction(para1,para2):
2  |    '''
3  |    Renvoie .....
4  |    Paramètres :
5  |    - para1 : ....
6  |    - para2 : ....
7  |    Valeur de retour : ...
8  |    Contraintes : 
9  |    - contr1 : ....
10 |    - contr2 : ....
11 |    Exemples :
12 |    >>> fonction(para1,para2) 
13 |    résultat
14 |    '''


"""

# Exemple 5 : Dans cet exemple il n'y a que les docstrings


def somme(a,b): 
    """
    >>> somme(6,5)
    11
    >>> somme(11,-11)
    0
    """
    return a + b


if __name__ == '__main__':
    import doctest 
    doctest.testmod(verbose=True)

"""
Dans le terminal :

Trying:
    somme(6,5)
Expecting:
    11
ok
Trying:
    somme(11,-11)
Expecting:
    0
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.somme
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

"""
import os 
# os.system("cls")  --> Pour nettoyer le terminal 