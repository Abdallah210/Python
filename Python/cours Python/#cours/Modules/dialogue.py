#coding:utf-8

def majuscule(Message):
    MessageMajuscule = ''
    for Lettre in Message :
        if Lettre.isalpha():
            if Lettre.isupper():
                MessageMajuscule += Lettre
            elif Lettre.islower():
                LettreMajuscule = Lettre.upper()
                MessageMajuscule += LettreMajuscule
        else :
            MessageMajuscule += Lettre
    return MessageMajuscule

def message(message):
    m = majuscule(message)
    print(m)

def cliquer():
    input()
    return None

def nom():
    NomJoueur = input("Insérez votre nom : ") 
    return NomJoueur


def choix():
    OuiNon = input('Réponse : ')
    return OuiNon


def parler(Persoone="Inconnue",message='...'):
    print("{} : {}".format(Persoone,message))
  

from random import choice 

ListeSalutation = ["Salut !", "Bonjour !"]
def Salutation(Saluer=choice(ListeSalutation),Ajout=''):
    return "{}{}".format(Saluer,Ajout)
    














"""

message("Tu reveilles dans un laboratoire")
cliquer()
parler(message=Salutation(Ajout="Finalement t'es reveillé !"))
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
parler("Toi",message=Choix())
parler("Dr.Abdallah", "Magnifique ! ")
cliquer()
parler("Toi", "Que ce je fait ici ?")
cliquer()
parler("Dr.Abdallah")

"""