#!/usr/bin/env python3 

from c4kapi import *
import random as r
cls()
anime(5)
nb = r.randint(0,10)
print(nb)
txt("J'ai choisi un nombre entre 0 et 10")
txt("Veux tu le trouver")
reponse = lire("oui ou non ? ")
if reponse!= "oui":
   txt("C'est pas grave")
   txt("bye bye")
   anime(7) 
   exit()
nb2=lire("Cherche le nombre: ")
txt("tu as dit:")
txt(nb2)
if nb2 == str(nb) :
    txt("bravo")
    anime(4)
else:
    anime(12)   
    txt("domage c'etait le nombre")
    txt(nb)
