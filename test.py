from flask import Flask, render_template, request
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *
from Classe.Tour import *
from tinydb import Query

id = 1

tournament = deserialiseTournoi(oneTournament(id))
tours = tournament.tournee
last_tour = oneTour(tours[-1])

# stockage de la liste des tours

list_matchs = []

b = 0
"""Boucle pour itérer la round et extraire chaque match de chaque round"""
for round in range(1, len(tours) + 1) :
    """ Iteration des round r pour en extraire les prochains matchs"""
    while b < 4:
        """ Extraction des id chaque match de chaque tour et le mettre dans une list"""
        m = recup_tour(id, "Round" + str(round))["match" + str(b+1)]
        m = m[:-1]
        list_matchs.append(m)
        b += 1
    b = 0

fauxmatchs = ['13','9']
for m in list_matchs:
    if fauxmatchs[0] == m[0] or fauxmatchs[0] == m[1]:
        if fauxmatchs[1] == m[0] or fauxmatchs[1] == m[1]:
            print("le match a eu lieu")
        else:
            print(" le match n'a pas eu lieu")
    else:
        print("le match n'a pas eu lieu")







