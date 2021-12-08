from flask import Flask, render_template, request
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *
from Classe.Tour import *

id = 1

tournament = deserialiseTournoi(oneTournament(id))
tours = tournament.tournee
last_tour = oneTour(tours[-1])

# stockage de la liste des tours


list_tours = []
list_matchs = []

b = 0
r = 0
"""Boucle pour iterer la round et extraire chaque match de chaque round"""
while r < 4:
    """ Iteration des round r pour en extraire les prochains matchs"""
    r += 1
    while b < 4:
        """ Extraction des id chaque match de chaque tour et le mettre dans une list"""
        list_matchs.append(recup_tour(id, "Round" + str(r))["match" + str(b+1)])
        b += 1
    b = 0



print(list_matchs)
# match_p1 = recup_tour(id, "Round" + str(1))["match1"]
# list_tours.append(recup_tour(id,"Round"+str(r)))
