from flask import Flask, render_template, request
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *
from Classe.Tour import *

app = Flask(__name__)

picFolder = os.path.join('static', 'image')
app.config['UPLOAD_FOLDER'] = picFolder


@app.route('/')
def index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpg')
    return render_template("index.html", logo_image=logo)


@app.route('/player_list')
def players():
    players = allPlayer()
    return render_template("player_list.html", players=players)


@app.route('/tournament_list')
def tournaments():
    tournaments = allTournament()
    return render_template("tournament_list.html", tournament=tournaments)


@app.route('/tournament_list/<id>')
def recapTournament(id):
    tournament = oneTournament(int(id))
    return render_template("recap_tournament.html", tournament=tournament)


@app.route('/start_tournament/<id>')
def StartTournament(id):
    tournament = deserialiseTournoi(oneTournament(int(id)))
    list_id = tournament.players
    listPlayers = []
    for i in list_id:
        listPlayers.append(OnePlayer(int(i)))

    match = {}
    matchdb = {}
    for p in range(4):
        #matchmaking
        match[str(len(match) + 1)] = [listPlayers[p], listPlayers[p + 4], None]
        matchdb[str(len(matchdb) + 1)] = [list_id[p], list_id[p + 4], None]
    #SI F5
    if not str(len(tournament.tournee)) in tournament.tournee:
        tour = Tour(id, "Round1",matchdb["1"],matchdb["2"],matchdb["3"],matchdb["4"])
        addTour(tour.serialise())
        tour = recup_tour(id, "Round1")
        tournament.tournee[str(len(tournament.tournee) + 1)] = tour.doc_id
        maj_tournoi(id, tournament)
    return render_template("start_tournament.html", match=match)


@app.route('/tour_progress/<id>', methods=['GET', 'POST'])
def Tour_progress(id):
    match1 = request.form['match1']
    match2 = request.form['match2']
    match3 = request.form['match3']
    match4 = request.form['match4']


    return render_template('tour_progress.html')
     #    if tour > 4:
    #    return render_template("fin_tournament.html")
    # else :
    #     return render_template('tour_progress.html')

@app.route('/player_list/<id>')
def recapPlayer(id):
    player = OnePlayer(int(id))
    return render_template("recap_player.html", joueur=player)


@app.route('/to_add_player')
def toAddPlayer():
    return render_template("add_player.html")


@app.route('/add_player', methods=['GET', 'POST'])
def playerAdd():
    if request.form['playerName'] == "" or request.form['playerFirstName'] == "" or request.form[
        'playerGender'] == "" or request.form['playerAge'] == "" or request.form['playerRanking'] == "":
        return render_template("add_player.html")
    else:
        nom = request.form['playerName']
        prenom = request.form["playerFirstName"]
        sexe = request.form["playerGender"]
        date = request.form["playerAge"]
        ranking = request.form["playerRanking"]
        new_player = Player(nom, prenom, sexe, date, ranking)
        addPlayer(new_player.serialise())
        return render_template("player_added.html")


@app.route('/to_add_tournament')
def toAddTournament():
    players = allPlayer()
    return render_template("add_tournament.html", players=players)


@app.route('/add_tournament', methods=['POST'])
def tournamentAdd():
    if request.form['tournamentName'] == "" or request.form['tournamentLocation'] == "" or request.form[
        'tournamentDate'] == "" or request.form['tournamentTour'] == "" or request.form['tournamentTimeControl'] == "":
        return render_template("add_tournament.html")
    else:
        name = request.form['tournamentName']
        location = request.form["tournamentLocation"]
        date = request.form["tournamentDate"]
        tours = request.form["tournamentTour"]
        timeControl = request.form["tournamentTimeControl"]
        player = []
        for p in range(1, 9):
            player.append(request.form["p" + str(p)])
        new_tournament = Tournament(name, location, date, timeControl, player, tours)
        addTournament(new_tournament.serialise())
        return render_template("tournament_added.html")


if __name__ == "__main__":
    app.run(debug=True)
