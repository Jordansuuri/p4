from flask import Flask, render_template, request
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *
from Classe.Tour import *

tour = dbTour.get(doc_id=1)
info_tour = []
for info in tour.values():
    info_tour.append(info)

round_number = info_tour[0]

info_match1 = info_tour[2]
id_player1_match1 = info_match1[0]
id_player2_match1 = info_match1[1]
resultat_match1 = info_match1[2]

tournament = deserialiseTournoi(oneTournament(int(id)))
list_id = tournament.players
listPlayers = []
for i in list_id:
    listPlayers.append(OnePlayer(int(i)))

match = {}

print(tour)