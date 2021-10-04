from tinydb import TinyDB, Query

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