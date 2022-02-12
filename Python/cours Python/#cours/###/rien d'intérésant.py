#coding:utf-8

def jeu():
    print("Jeux disponibles :\n1.Street Fighters (1)\n2.Nemo (2)")
    jeu = ''
    while jeu != 1 and jeu != 2 :
        jeu = int(input("\ninsérez le numero du jeu : "))
        if jeu == 1 :
            print("STREET FIGHTERS !")
            return "Street Fighters"
        elif jeu == 2 :
            print("NEMO !")
            return "Nemo"
        else:
            print("Le numéro inséré est inccoret")



def présentation():
    NomJeu = jeu()
    if NomJeu == "Street Fighters":
        print("Ce jeu est fait pour vous ! {} est un jeu de combat".format(NomJeu))
    else:
        print("Ce jeu est fait pour vous ! {} est un jeu d'avventure".format(NomJeu))


présentation()