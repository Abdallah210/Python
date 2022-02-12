#coding:utf-8

#5 Les conditions

"""
Mots clés des conditions :  if   (si)
                            elif (sinon si)
                            else (sinon)


Après ces mots, on écrit des expressions booléens .

Expressions booléens : True  (Vrai)
                       False (Faux)


Les conditions multiples : not     (pas)
                           and     (et)
                           or      (ou)
                           in      (dans)
                           not in  (pas dans)


Opérateurs de comparaison : == (égal à)
                            != (différent à)
                            <  (plus petit à)
                            >  (plus grand que)
                            <= (plus petit que ou égal à)
                            >= (plus grand que ou égal à)


les conditions multiples et les opérateurs de comparaisons aident à écrire des expression booléens  
Expressions booléens : True  (Vrai)
                       1 != 0  (True)


"""

# Exemple 1 : ____________________________________________________________________________
print("\nExemple 1 : ")  # Validité de la première condition

if True :
    print("exemple 1 : condition 1 vérifiée")
else:
    print("exemple 1 : condition 2 vérifiée")



# Exemple 2 : ______________________________________________________________________________
print("\nExemple 2 : ")  # Validité de la seconde condition

if False :
    print("exemple 2 : condition 1 vérifiée")
else :
    print("exemple 2 : condition 2 vérifiée")



# Exemple 3 : _______________________________________________________________________________
print("\nExemple 3 : ")  # Utilisation de (if), (elif) et (else)

age = int(input("insérez votre age : "))

if age <= 0 or age >= 101 :
    print("l'age inséré est incorrect .")
elif age < 18 :
    print("Vous êtes minoré !")
else :
    print("Vous êtes majoré !") 



# Exemple 4 : _______________________________________________________________________________
print("\nExemple 4 : ") # Utilisation de (in)

lettre = input("choissisez un seule lettre : ")

if lettre in "aeiouy" :    
    print("le lettre chosit est une voyelle . ")
else :
    print("le lettre chosit est une consonne . ")

# Avec (not in),il vérifiera l'autre condition 




# Exemple 5 : _______________________________________________________________________________
print("\nExemple 5 : ") # Utilisation de (not) et (or)

nombre = int(input("insérer un nombre : "))

if not nombre < 0 or not nombre < 0.0 :
    print("le nombre inséré est positif")
elif not nombre > 0 or not nombre > 0.0  :     
    print("le nombre inséré est négatif") 
else :
    print("le nombre inséré est nul") 





# Exemple 6 :
print("\nExemple 6 : ")


print(" ")
heures = int(input("heures : "))
minutes = int(input("Minutes : "))
