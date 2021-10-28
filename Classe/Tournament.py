
class Tournament:
	"""initialise le nom, l'emplacement et la date du tournoi"""
	def __init__(self, name, location, date, timeControl, player, tours = 4, tournee ={}):
		self.nom = name
		self.localisation = location
		self.date = date
		self.tours = tours
		self.tournee = tournee
		self.timeControl = timeControl
		self.players = player


	def serialise(self):
		return {'nom': self.nom, 'localisation': self.localisation, 'date': self.date, 'tours': self.tours, 'tournee': self.tournee, 'timeControl': self.timeControl, 'players': self.players}

def deserialiseTournoi(tournoi):
	nom = tournoi['nom']
	localisation = tournoi['localisation']
	date = tournoi['date']
	tours = tournoi['tours']
	tournee = tournoi['tournee']
	timeControl = tournoi['timeControl']
	players = tournoi['players']
	return Tournament(nom, localisation, date, timeControl, players, tours, tournee)