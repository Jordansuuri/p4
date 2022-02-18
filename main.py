from flask import Flask, render_template, request, redirect
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *
from Classe.Tour import *
from operator import itemgetter

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
    tournament = oneTournament(id)
    return render_template("recap_tournament.html", tournament=tournament)


@app.route('/start_tournament/<id>')
def StartTournament(id):
    """ Récupération du tournoi en deserialisant le tournois dans un objet auparavant en json"""
    tournament = deserialiseTournoi(oneTournament(id))
    if len(tournament.tournee) > 0:
        return redirect('/tour_progress/'+id)
    """ Récupération de la liste des ID des joueurs """
    list_id = tournament.players
    # TRIER LISTE ID PAR RAPPORT AU CLASSEMENT
    #Utiliser sort
    listPlayers = []
    """ Ajout des id des joueurs dans une liste (listPlayers) """
    for i in list_id:
        listPlayers.append(OnePlayer(i))
    """Création d'un classement intermediaire"""

    ranking_inter = []
    for i in range(len(list_id)):
        ranking_inter.append([list_id[i], listPlayers[i]["ranking"], 0])

    """Creation de deux dictionnaires, match & matchdb"""
    match = {}
    matchdb = {}
    for p in range(4):
        """" Création des différents matchs (matchmakking) avec en simultanée l'id et le nom du joueur"""
        match[str(len(match) + 1)] = [listPlayers[p], listPlayers[p + 4], None]
        matchdb[str(len(matchdb) + 1)] = [list_id[p], list_id[p + 4], None]
    """ Securité afin que l'utilisateur n'abuses pas du refresh de la page"""
    if not str(len(tournament.tournee)) in tournament.tournee:
        """Creation de l'objet tour qui appelle la premier fonction"""
        #Recuperation de l'heure du tour afin de l'intergrer a la variable "tour"
        tour = Tour(id, "Round" + str(len(tournament.tournee) + 1), matchdb["1"], matchdb["2"], matchdb["3"],
                    matchdb["4"], ranking_inter)
        """Enregistrement du tour dans la base de donnée"""
        addTour(tour.serialise())
        tour = recup_tour(id, "Round" + str(len(tournament.tournee) + 1))
        """ Enregistrement de l'id du round dans l'objet tournoi"""
        tournament.tournee.append(tour.doc_id)
        maj_tournoi(id, tournament)
    return render_template("start_tournament.html", match=match, tournament=oneTournament(id))


@app.route('/tour_progress/<id>', methods=['GET', 'POST'])
def Tour_progress(id):
    """Recupération du tournoi"""
    tournament = deserialiseTournoi(oneTournament(id))
    """Récupération des id du dernier tour"""
    tours = tournament.tournee
    """Recupération du dernier tour dans le tableau tournee"""
    # ajout date & heure de fin
    last_tour = oneTour(tours[-1])
    if len(tours) == tournament.nb_tours:
        return redirect("/fin_tournoi/"+id)
    if len(request.form) > 0:
        ranking_inter = last_tour["ranking"]
        """Affectation du résultat de chaque match"""
        last_tour["match1"][2] = request.form['match1']
        last_tour["match2"][2] = request.form['match2']
        last_tour["match3"][2] = request.form['match3']
        last_tour["match4"][2] = request.form['match4']
        # Ici on doit ajouter le nombre de points aux gagnants & aux pats (classement intermediaire) [[id,classement, nbPoints],[etc,etc,etc] x8
        # Ajouter à tour ligne 162
        """Enrengistrement du tour avec maj_tournoi"""
        # ajout du classement & date de fin dans le MAJ tour
        majTour(tours[-1], last_tour)

        """Création d'une liste afin de stocker les id des joueurs gagnants d'abord"""
        rematch_list = []
        for p in range(4):
            id_vainqueur = last_tour['match' + str(p + 1)][2]
            if id_vainqueur != "pat":
                print("id du vainqueur : " + id_vainqueur)
                # boucle sur ranking_inter pour chercher l'id du vainqueur (indice 0) pour modifier le score interne (indice 2)
                # pour chaque tableau dans ranking_inter
                #    est-ce que id_vainqueur est égal à l'indice 0 du tableau
                #  si oui augmente indice 2 de +1
                # si non (rien à faire) car ça va tester le tableau suivant
                for r in ranking_inter:
                    if id_vainqueur == r[0]:
                        r[2] += 1
            else:
                id_j1 = last_tour['match' + str(p + 1)][0]
                id_j2 = last_tour['match' + str(p + 1)][1]
                for r in ranking_inter:
                    if id_j1 == r[0]:
                        r[2] += 0.5
                    if id_j2 == r[0]:
                        r[2] += 0.5
            print(ranking_inter)
        ranking_done = sorted(ranking_inter, key=itemgetter(2), reverse=True)
        print(ranking_done)

     # tu crée rematch_list qui ne va contenir que les id des joueurs dans l'ordre voulu (attention ranking_inter est alors classé!)
        for j in ranking_done:
            rematch_list.append(j[0])
        """ puis perdant par la suite afin de les faire jouer entre eux """
        #ajout fonction pat? si joueur 1 ou 2 etc #

        list_matchs = []
        b = 0


        """Boucle pour itérer la round et extraire chaque match de chaque round"""
        for id_tour in tours:
            t = oneTour(id_tour)
            """recuperation de tour par rapport à son ID"""
            while b < 4:
                """ Extraction des id chaque match de chaque tour et le mettre dans une list"""
                m = t["match" + str(b + 1)]
                m = m[:-1]
                list_matchs.append(m)
                b += 1
            b = 0

        nouveau_match = {}
        matchtemplate = {}

        for j in range(4):
            matchok = False
            i = 1
            print(rematch_list)
            while not matchok and i < len(rematch_list):
                match = [rematch_list[0],rematch_list[i]]
                """verification que le match a déjà eu lieu"""
                for m in list_matchs:
                    if match[0] == m[0] or match[0] == m[1]:
                        if match[1] == m[0] or match[1] == m[1]:
                            i += 1
                            matchok = False
                        else:
                            matchok = True
                    else:
                        matchok = True
            """" Création des différents matchs (matchmakking) avec en simultanée l'id et le nom du joueur"""
            nouveau_match[str(j + 1)] = [match[0], match[1], None]
            matchtemplate[str(len(matchtemplate) + 1)] = [OnePlayer(match[0]), OnePlayer(match[1]),None]

            del rematch_list[0]
            if i > len(rematch_list):
                i = len(rematch_list)
            del rematch_list[i-1]

        #if int(id) == len(tournament.tournee): # sécurisation de la route pour éviter d'enregistrer des tours vides
        """Creation de l'objet tour qui appelle la premier fonction"""
        tour = Tour(id, request.form['name_tour'], nouveau_match["1"], nouveau_match["2"], nouveau_match["3"],
                    nouveau_match["4"], ranking_done)
        """Enregistrement du tour dans la base de donnée"""
        addTour(tour.serialise())
        tour = recup_tour(id,request.form['name_tour'])
        numero_tour = len(tournament.tournee) + 1
        """ Enrengistrement de l'id du round dans l'objet tournoi"""
        tournament.tournee.append(tour.doc_id)
        maj_tournoi(id, tournament)
    else:
        matchtemplate = {}
        for m in range(1,5):
            match = last_tour['match'+str(m)]
            matchtemplate[str(len(matchtemplate) + 1)] = [OnePlayer(match[0]), OnePlayer(match[1]), None]
        numero_tour = len(tournament.tournee) + 1

    #verifier la longueur de tournament.tournee si tournamement.tournee est superieur a tournament.tour => rediriger vers fin du tournoi (recap des differents rounds : definir vainqueur tournoi)
    return render_template('tour_progress.html', match=matchtemplate, tournament=oneTournament(id), numero_tour=numero_tour)


@app.route('/player_list/<id>')
def recapPlayer(id):
    player = OnePlayer(id)
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
