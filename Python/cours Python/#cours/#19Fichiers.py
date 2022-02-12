#45 Les Fichiers :

"""
Sommaire :

Partie 1 : Différents types de fichiers
                                                        
        I  - les fichiers textes 
        II - les fichiers binaire


Partie 2 : Lire, écrire dans des fichiers en python 

    I  - Ouverture d'un canal de communication 
            1- mode d'ouverture
            2- la fonction open(str1, str2)
            3- Schéma


    II  - Fermature d'un canal de communication 
            1- La méthode .close()
            2- Type d'un canal ouvert

    III - Structure syntaxique et lecture 
            1- Forme syntaxique with...as...
            2- La méthode .readline() 
            3- La méthode .readlines()
            4- La méthode .read()
            5- Impossible de lire

    IV - Ecriture
            1- Écrire des chaînes de caractères
            2- Écrire des lignes
            3- Impossible d’écrire

Partie 3 : Exemples

Partie 4 : Codage des fichiers textes

Partie 5 : Les canaux standards :
    1- Canal standard de lecture
    2- Canal standard d'écriture
    3- La fonction input

Partie 6 : Traitement des données lues
    1- Retour sur les exceptions
    2- Le loup entre dans la bergerie
    3- L’instruction try ... except ou comment repousser le loup ?
    4- Vers une meilleure version de la fonction lire_date


"""




# Partie 1 :
"""
Différants types de fichiers :
    I  - Les fichiers textes
    II - Les fichiers binaires


I - Les fichiers textes : 

Les fichiers textes sont ceux qui contenant du texte 


Exemples : 
+ fichiers textes bruts (plain text)    : .docx, .txt ...  
+ fichiers source de programmes         : .js, .py, .php ...
+ fichiers HTML et CSS                  : .html, .css
+ fichiers CSV (format tableur textuel) : .xls ...



La structure que partagent tous ces formats de fichiers textes est celle de ligne

  + ligne == chaîne de caractères terminée par un marqueur de fin ligne (n\)
  + marquer de fin ligne == (n\)


Le principal outil informatique pour lire/produire un fichier texte est un éditeur de texte (Visual Studio Code ...). 




II - Les fichiers binaires :

On déclare binaire tout fichier qui n’est pas un fichier texte.


+ fichiers exécutables résultant de la compilation d’un fichier texte source
+ fichiers archives  : .zip, .tgz ...
+ fichiers images    : .png, .jpg, .gif, .tiff ... 
+ fichiers sons      : .mp3, .ogg, .flac, .wav ...
+ fichiers videos    : .mp4, .avi, .mpeg ... 

Contrairement aux fichiers textes pour lesquels la structure de ligne est une structure commune, 
il n’y a pas de structure commune à tous les fichiers binaires. Les outils informatiques pour l
ire/produire les fichiers binaires dépendent évidemment du format de ces fichiers.



+---------------------------------------------------------------------------------------------+
|    Type de fichiers    |  marqueur de fin ligne (n\)  |           lire/produire             |
+---------------------------------------------------------------------------------------------+
|         textes         |             oui              |          éditeur de texte           |
+---------------------------------------------------------------------------------------------+
|         binaire        |             non              |    dépant format de ces fichiers    |
+---------------------------------------------------------------------------------------------+
"""




# Partie 2 : Lire, écrire dans des fichiers en python :

"""

I - Ouverture d'un canal de communication :


L’ouverture d’un canal peut se faire :
   1- Mode lecture              : on peut que lire les infos contenues dans le fichier
   2- Mode écriture             : il n'est possible que écrire dans le fichier
   3- Mode lecture et écriture  : on peut lire les infos et écrire dans le fichier au même temps




Pour ouvrir les cannaux en Python, on utilise la fonction open(srt1, str2) 

La fonction open(str1, str2) : prend deux chaîne de caractères str1  et str2
                               - str1 --> le nom du fichier à ouvrir
                               - str2 --> le mode d'ouverture
                               - mode d'ouverture: 
                                  1. mode lecture                : 'rt' ou 'r' (r=read et t=text)
                                  2. mode écriture (dangereuse)  : 'wt' ou 'w' (w=write et t=text)
                                  3. mode écriture (en sécurité) : 'x'
                                  4. mode ajout                  : 'a' (a=append)
                                  5. mode ???                    : '+' avant 'r', 'w' , 'x', et 'a'


'r' pour une ouverture en lecture (READ).
'w' pour une ouverture en écriture (WRITE), à chaque ouverture le contenu du fichier est écrasé. Si le fichier n'existe pas python le crée.
'a' pour une ouverture en mode ajout à la fin du fichier (APPEND). Si le fichier n'existe pas python le crée.
'b' pour une ouverture en mode binaire.
't' pour une ouverture en mode texte.
'x' crée un nouveau fichier et l'ouvre pour écriture


Avertissement ! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + Si le fichier qu’on veut ouvrir n’existe pas une exception 'FileNotFoundError' est déclenchée.

    + L’ouverture en écriture d’un canal vers un fichier existant entraîne la perte des données que contenait ce fichier. 
      donc l'ouverture en mode 'w' est donc une opération potentiellement dangereuse.

    + Si on ouvre un canal vers un fichier non existant avec 'a', un nouveau est créé

    + 'w' == 'wt' et 'r' == 'rt' (texte)

    + 'wb' et  'rb'  (binaire)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Schéma explicatif:
_______________________________________________________


 (Périphérique)                           (Mémoire)
 |           |          écriture        |           |
 |           |   <===================   |           |
 |  fichier  |  canal de communication  | processus |
 |           |   ===================>   |           |
 |           |          lecture         |           |

________________________________________________________







II - Fermature d'un canal de communication :


Pour fermer un canal, on utilise la méthode .close()


.close() n'a aucune relation entre entree et sortie
entree  -->  read   (faire entrer les donneés et les lire)
sortie  -->  write  (créer des données est les faire sortir)


____________________________________________

entree = open('existe.bien', 'r')
sortie = open('existe.bien', 'w')

entree.close()
sortie.close()

____________________________________________

Avertissement ! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + L’oubli de fermeture d’un canal ouvert en écriture peut entraîner la perte de données. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Type d'un canal ouvert sur un fichier texte : 
___________________________________________
entree = open('existe.bien', 'r')
sortie = open('existe.bien', 'w')


>> type(entree)
<class '_io.TextIOWrapper'>

>> type(sortie)
<class '_io.TextIOWrapper'>
___________________________________________



La méthode .read() : 
    - permet de lire le contenu du fichier qui est ouvert en mode de lecture
    - ne fonctione pas avec un fichier ouvert avec le mode écriture 



"""

#Ouverture en mode lecture :
entree = open('#19xlecture.txt', 'r')


#Ouverture en mode écriture :
sortie = open('#19xecriture.txt', 'w')


entree  #<_io.TextIOWrapper name='lecture.txt' mode='r' encoding='cp1252'>
sortie  #<_io.TextIOWrapper name='ecriture.txt' mode='w' encoding='cp1252'>




"""
III - Structure syntaxique et lecture 


1- Forme syntaxique (with...as...) :

Python offre une structure syntaxique qui permet d'omettre la commande explicite (clair/précis) du fermature d'un canal
Cette structure syntaxique est : with...as...


Syntaxe : with open('nomfichier.txt', 'r') as x


L'identificateur qui se trouve après 'as' (x) est le nom donné au canal ouvert par open('nomfichier.txt', 'r')

______________________________________________________________________________________
-                                                                                    |
Après la structure, on indente les instructions après en créant un bloc              |
En sortant du bloc, le canal ouvert est automatiquement férmé                        |
-                                                                                    |
1) ______________________________________________                                    |
-                                                |                                   |
instr... (avant le bloc)                         |                                   |
-                                                |                                   |
with open(str1, str2) as x                       |                                   |
    instr1...     |                              |                                   |
    instr2...     | <-- bloc                     |                                   |
    ...           |                              |                                   |
-                                                |                                   |
instr... (après le bloc)     #sortie du bloc     |                                   |
_________________________________________________|                                   |
-                                                                                    |
De cette façon, les lignes précédentes sont équivalentes aux suivantes :             |
2) ______________________________________________                                    |
-                                                |                                   |
# instr avant                                    |                                   |
-                                                |                                   |
x = open(str1, str2)                             |                                   |
traitement... sur x                              |                                   |
x.close()                                        |                                   |
-                                                |                                   |
# instr après                                    |                                   |
_________________________________________________|                                   |
-                                                                                    |
______________________________________________________________________________________


"""

"""
2- La méthode .readline() :

La méthode .readline() que possèdent les canaux ouverts en lecture 
Renvoie la première ligne sur laquelle pointe actuellement le canal.

A chaque fois on appelle la méthode .readline() le canal pointe la ligne précédente

Avertissement !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + Quand le canal pointe la dernière ligne et on ajoute un autre appel l'expression va envoyer un chaîne vide ''
    C-à-d Si : 
    on appelle entree.readline() n fois (n > nombre de ligne) -->  entree.readline() == ''

    + Si le canal pointe une ligne vide signifie pas que l'expression va envoyer une chaîne vide
    C-à-d Si : 
    la ligne pointée par le canal est vide  -->  entree.readline() == '\n'

    + Si on ferme le canal de communication et on le réouvre, le canal pointe de nouveau la première ligne

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

entree = open('#19x3ligne.txt', 'r')  #ouverture du canal en lecture (read)


# premier appel de .readline()

ligne1 = entree.readline()
ligne1  # 'ligne 1 n\'  (str)


# deuxième appel de .readline()

ligne2 = entree.readline()
ligne2  # 'ligne 2 n\'  (str)


# troisième appel de .readline()

ligne3 = entree.readline()
ligne3  # 'ligne 3 '  (str)


entree.close()




"""
3- La méthode .readlines() :

La méthode .readlines() donne une où les chaque ligne devient un éléments d'elle sous forme dune chaîne de caractères

"""

entree = open('#19x3ligne.txt', 'r')  # ouverture du canal en lecture (read)

lignes = entree.readlines()

lignes  # ['ligne 1 \n', 'ligne 2 \n', 'ligne 3 ']



entree.close()




"""
4- La méthode .read(entier) :

La méthode .read(entier) ne respecte pas la structure en lignes des fichiers textes et elle peut s’employer avec ou sans
paramètre 'entier' 

Avertissement : ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
    + Avec la méthode .read() le canal pointe les caractères et ne pas les lignes

    + Le paramètre 'entier' doit être positif

    + on peut caster les valeurs avec int() pour utiliser les données du fichiers dans le calcule

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

entree = open('#19x3ligne.txt', 'r')  # ouverture du canal en lecture (read)


# Avec paramètre 'entier' :

appel1 = entree.read(3) # 
appel1   # 'lig'


appel2 = entree.read(10) 
appel2   # 'ne 1 \nlign'

# Sans paramètre 'entier' : 
"""Il va renvoyer tous les caractères qui se trouve après le caractère pointé par le canal"""
appel3 = entree.read()  
appel3   # 'e 2 \nligne 3 '

entree.close()


"""
Résumé des méthodes de lecture :
+--------------------------------------------------------------------------------------+
|      méthodes     |   Valeur de retour   |     paramètre     |   pointage du canal   |
+--------------------------------------------------------------------------------------+
|      .read()      |          str         |        oui        |       caractère       |
+--------------------------------------------------------------------------------------+
|    .readline()    |          str         |        non        |         ligne         |
+--------------------------------------------------------------------------------------+
|    .readlines()   |          list        |        non        |         ligne         |
+--------------------------------------------------------------------------------------+
"""



"""

5- Impossible de lire :

Quelle que soit la méthode (.read(), .readline() ou .readlines()), Il est impossible de lire un fichier ouvert en écriture.

_____________________________________________
entree = open('#45x3ligne.txt', 'w')

x = entree.read()
>> x
io.UnsupportedOperation: not readable
_____________________________________________

"""


"""
IV - Ecriture :


1- Écrire des chaînes de caractères : La méthode .write(str)

Avec la méthode .write(str), on peut écrire n’importe quelle chaîne de caractères dans un fichier.

Avertissement ! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + l'expression sortie.write(str) renvoie combien de caractère ajoutés au fichier
    C-à-d :  sortie.write(str) == len(str)
             type(sortie.write(str)) == < class 'int'>

    + le marqueur de fin ligne est considéré un seul caractère
    C-à-d :  len('\n') == 1

    Aussi pour :  \n est un marqueur fin de ligne
                  \t est une tabulation
                  \b est un « backspace »
                  \a est un « bip »
                  \' est un « ' », mais il ne ferme pas la chaine de caractères
                  \" est un « " », mais il ne ferme pas la chaine de caractères
                  \\ est un « \ »
    
    + on peut caster les valeurs str() pour les écrire dans un fichiers

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

sortie = open('#19xméthodewrite.txt', 'w')

ecrit1 = sortie.write('Timoleon est un homme politique')
ecrit1  #31

ecrit2 = sortie.write(' grec\nLa deuxième ligne !' )
ecrit2  #25

sortie.close()


"""
2- La méthode .writelines(list) :

La méthode .writelines(list) permet d’écrire dans un fichier une liste de chaînes de 
caractères. 

Avertissement ! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    + Si chacune de ces chaînes se termine par un marqueur de fin de ligne, le nombre de lignes écrites dans le fichier 
    est égal à la longueur de la liste.
    C-à-d :  nombre de lignes == n*'\n' (n répétition de '\n')

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



with open('#19xméthodewritelines.txt', 'w') as sortie :

    ecrit = sortie.writelines(["bonjours\n","ligne2\n", "ligne3\n", "dernière ligne, bye !\n"])
    #pas besoin de fermer le canal 'w'



"""
Résumé des méthodes de lecture :
+-------------------------------------------------------------------------------------------+
|      méthodes      |   Valeur de retour   |   type du paramètre   |   pointage du canal   |
+-------------------------------------------------------------------------------------------+
|      .write()      |          int         |           str         |       caractère       |
+-------------------------------------------------------------------------------------------+
|    .writelines()   |         None         |           list        |       caractère       |
+-------------------------------------------------------------------------------------------+
"""



"""
3- Impossible d’écrire :

Il est impossible d’écrire (quelque soit la méthode) dans un fichier ouvert en lecture.

_____________________________________________
sortie = open('#45x3ligne.txt', 'r')

x = sortie.write(str)
>> x
io.UnsupportedOperation: not readable
_____________________________________________

"""




#Partie 3 : Exemples
"""
"""











#Partie 4 : Codage des fichiers textes





#Partie 5 : Les canaux standards :

"""
    1- Canal standard de lecture
    2- Canal standard d'écriture
    3- La fonction input




"""

#Partie 6 : Traitement des données lues

"""
    1- Retour sur les exceptions
    2- Le loup entre dans la bergerie
    3- L’instruction try ... except ou comment repousser le loup ?
    4- Vers une meilleure version de la fonction lire_date

"""