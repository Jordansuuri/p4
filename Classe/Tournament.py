
class Tournament:
	"""initialise le nom, l'emplacement et la date du tournoi"""
	def __init__(self, name, location, date, timeControl, player, nb_tours = 4, tournee =[]):
		self.nom = name
		self.localisation = location
		self.date = date
		self.nb_tours = nb_tours
		""" Sous forme de tableau qui contient les doc_id des tours"""
		self.tournee = tournee
		self.timeControl = timeControl
		""" Sous forme de tableau qui contient les doc_id des joueurs"""
		self.players = player


	def serialise(self):
		return {'nom': self.nom, 'localisation': self.localisation, 'date': self.date, 'nb_tours': self.nb_tours, 'tournee': self.tournee, 'timeControl': self.timeControl, 'players': self.players}

def deserialiseTournoi(tournoi):
	nom = tournoi['nom']
	localisation = tournoi['localisation']
	date = tournoi['date']
	nb_tours = tournoi['nb_tours']
	tournee = tournoi['tournee']
	timeControl = tournoi['timeControl']
	players = tournoi['players']
	return Tournament(nom, localisation, date, timeControl, players, nb_tours, tournee)