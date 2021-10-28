from tinydb import TinyDB
from tinydb.table import Document

dbPlayer = TinyDB('DB/player.json')
dbTournament = TinyDB('DB/tournament.json')

def allPlayer():
    players = dbPlayer.all()
    return players

def OnePlayer(id):
    player = dbPlayer.get(doc_id=id)
    return player

def allTournament():
    tournaments = dbTournament.all()
    return tournaments

def oneTournament(id):
    tournament = dbTournament.get(doc_id=id)
    return tournament

def addPlayer(player):
    dbPlayer.insert(player)

def addTournament(tournament):
    dbTournament.insert(tournament)

def maj_tournoi(id, tournament):
    dbTournament.remove(doc_ids=[int(id)])
    dbTournament.insert(Document(tournament.serialise(), doc_id=id))
