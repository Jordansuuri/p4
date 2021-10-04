from tinydb import TinyDB, Query

dbPlayer = TinyDB('player.json')
dbTournament = TinyDB('tournament.json')


dbPlayer.insert({'prenom':'Hugo',  'nom': 'x', 'age':'29', 'ranking':'1150'})
dbPlayer.insert({'prenom':'Nicolas','nom': 'x', 'age':'34', 'ranking':'1240'})
dbPlayer.insert({'prenom':'Guillaume','nom': 'x', 'age':'30', 'ranking':'1190'})
dbPlayer.insert({'prenom':'Martin','nom': 'x', 'age':'29', 'ranking':'1050'})

dbTournament.insert({'name':'Tournoi2015','location':'Paris','date':'02/08/21','tour':'4'})

#affichage des joueurs & tournois
for player in dbPlayer:
    print(player)

for tournament in dbTournament:
    print(tournament)
