from flask import Flask,render_template, request
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *

app = Flask(__name__)

picFolder = os.path.join('static','image')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'],'logo.jpg')
    return render_template("index.html", logo_image = logo)


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
    listeid = tournament.players
    listeJoueurs = []
    for i in listeid:
        listeJoueurs.append(OnePlayer(int(i)))

    match = {}
    for p in range(4):
        match[str(len(match)+1)] = [listeJoueurs[p],listeJoueurs[p+4],None]
    if not str(len(tournament.tournee)) in tournament.tournee:
        tournament.tournee[str(len(tournament.tournee) + 1)] = match
        maj_tournoi(id, tournament)
    return render_template("start_tournament.html", match=match)

@app.route('/player_list/<id>')
def recapPlayer(id):
    player = OnePlayer(int(id))
    return render_template("recap_player.html", joueur=player)

@app.route('/to_add_player')
def toAddPlayer():
    return render_template("add_player.html")

@app.route('/add_player', methods=['GET','POST'])
def playerAdd():
    if request.form['playerName'] == "" or request.form['playerFirstName'] == "" or request.form['playerGender'] == "" or request.form['playerAge'] == "" or request.form['playerRanking'] == "":
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
    if request.form['tournamentName'] == "" or request.form['tournamentLocation'] == "" or request.form['tournamentDate'] == "" or request.form['tournamentTour'] == ""  or request.form['tournamentTimeControl'] == "" :
        return render_template("add_tournament.html")
    else :
        name = request.form['tournamentName']
        location = request.form["tournamentLocation"]
        date = request.form["tournamentDate"]
        tours = request.form["tournamentTour"]
        timeControl = request.form["tournamentTimeControl"]
        player = []
        for p in range(1,9):
            player.append(request.form["p"+str(p)])
        new_tournament = Tournament(name, location, date, timeControl, player, tours)
        addTournament(new_tournament.serialise())
        return render_template("tournament_added.html")


if __name__ == "__main__":
    app.run(debug=True)


