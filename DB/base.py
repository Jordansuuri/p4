from tinydb import TinyDB, Query
from tinydb.table import Document

dbPlayer = TinyDB('DB/player.json')
dbTournament = TinyDB('DB/tournament.json')
dbTour = TinyDB('DB/tour.json')


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


def addTour(result_tour):
    dbTour.insert(result_tour)


def recup_tour(id, nom):
    req = Query()
    return dbTour.get(req.idtournoi == id and req.nom == nom)

def oneTour(id):
    tour = dbTour.get(doc_id=int(id))
    return tour

def majTour(id, tour):
    dbTour.remove(doc_ids=[int(id)])
    dbTour.insert(Document(tour, doc_id=id))
