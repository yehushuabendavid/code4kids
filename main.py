from c4kapi import *
cls();
txt("Code 4 Kids te dit:")
txt("Bonjour")
nom=lire("Comment tu t'appelles? " )
joue=lire("Veux tu jouer "+nom +"? ")
if joue=="oui":
    txt("C'est parti")
    while True:
        a = lire("Lance une anime (1 a 12): ")
        if a=="non":
            break
        anime(a)
else:
    txt("domage "+ nom +" !!")

cls()
txt("Bye bye")
