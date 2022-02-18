from flask import Flask, render_template, request
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *
from Classe.Tour import *
from tinydb import Query
from operator import itemgetter

id = 1

tournament = deserialiseTournoi(oneTournament(id))
tours = tournament.tournee
last_tour = oneTour(tours[-1])
list_matchs = []

ranking_inter = [['7', '1500', 1], ['8', '1500', 1], ['9', '1500', 0.5], ['10', '1500', 0], ['11', '1500', 0], ['12', '1500', 0.5], ['13', '1500', 0], ['14', '1500', 1]]

last_tour = oneTour(tours[-2])
p = 0
id_vainqueur = last_tour['match'+str(p+1)][2]

#
#for p in range(4):
#    id_vainqueur = last_tour['match' + str(p+1)][2]
#    if id_vainqueur != "pat":
#        # boucle sur ranking_inter pour chercher l'id du vainqueur (indice 0) pour modifier le score interne (indice 2)
#        # pour chaque tableau dans ranking_inter
#        #    est-ce que id_vainqueur est égal à l'indice 0 du tableau
#        #  si oui augmente indice 2 de +1
#        # si non (rien à faire) car ça va tester le tableau suivant
#        for r in ranking_inter:
#            if id_vainqueur == r[0]:
#                r[2] += 1
#    else:
#        id_j1 = last_tour['match' + str(p + 1)][0]
#        id_j2 = last_tour['match' + str(p + 1)][1]
#        for r in ranking_inter:
#            if id_j1 == r[0]:
#                r[2] += 0.5
#            if id_j2 == r[0]:
#                r[2] += 0.5

        # ranking_inter[n][2] = + 0.5 ajouter 0.5 à chaque joueur qui a fait pat
        # récuperer les id des deux joueurs du match et tu vas boucler sur ranking_inter pour ajouter 0.5
         # une fois que les scores internes sont mis à jour, il faut classer le ranking_inter en fonction du score interne



# classement de ranking inter
# exporter ranking_inter[0,1,2,3,4 etc]
# création d'une liste vide ranking_compare qui va se remplir des valeurs en comparant ranking inter
# boucle dans une boucle qui va parcourir ranking_inter puis la nouvelle liste
# condition si plus grand ou moins grand : utiliser la fonction insert
#transformer sous forme de fonction et utiliser l'arguement (ranking_inter) qui est la liste a trier
#for element in tableau 1:
#	for i in range(len(tab2)):
#		if elem[2] > tab2[i][2]:
#			insert()

ranking_done = []

#for elem in ranking_inter:
#    if elem[2] > ranking_done[i][2]:
#        insert "element plus petit"
#        print(elem[2]+"ajouté dans ranking_done")
#        print(ranking_done)
#    else :
#        append "elementplusgrand"
#        print(elem[2] + "ajouté dans ranking_done")
#        print(ranking_done)


ranking_inter = [['7', '1500', 1], ['8', '1500', 1], ['9', '1500', 0.5], ['10', '1500', 0], ['11', '1500', 0], ['12', '1500', 0.5], ['13', '1500', 0], ['14', '1500', 1]]
ranking_done = sorted(ranking_inter, key=itemgetter(2), reverse = True)
print(ranking_done)

print(tournament.tournee)