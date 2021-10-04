from flask import Flask,render_template, request
from DB.base import *
import os
from Classe.Player import *

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
    return render_template("tournament_list.html", tournois=tournaments)


@app.route('/player_list/<id>')
def recapPlayer(id):
    player = OnePlayer(int(id))
    return render_template("recap_player.html", joueur=player)

@app.route('/player_add', methods=['POST'])
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


@app.route('/add_tournament', methods=['POST'])
def tournamentAdd():
        name = request.form['tournamentName']
        location = request.form["tournamentLocation"]
        date = request.form["tournamentDate"]
        tours = request.form["tournamentTour"]
        tournee = request.form["tournamentTournee"]
        timeControl = request.form["tournamentTimeControl"]
        new_tournament = Player(name, location, date, tours, tournee, timeControl)
        addTournament(new_tournament.serialise())
        return render_template("tournament_added.html")


if __name__ == "__main__":
    app.run(debug=True)

