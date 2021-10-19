
class Tournament:
	"""initialise le nom, l'emplacement et la date du tournoi"""
	def __init__(self, name, location, date, timeControl, player, tours = 4):
		self.nom = name
		self.localisation = location
		self.date = date
		self.tours = tours
		self.tournee = []
		self.timeControl = timeControl
		self.players = player


	def serialise(self):
		return {'nom': self.nom, 'Localisation': self.localisation, 'date': self.date, 'tours': self.tours, 'tournee': self.tournee, 'timeControl': self.timeControl, 'players': self.players}


