from Class.tinydb import TinyDB

class Tournament:
	"""initialise le nom, l'emplacement et la date du tournoi"""
	def __init__(self, name, location, date, tours = 4, tournee, timeControl):
		self.name = name
		self.location = location
		self.date = date
		self.tours = tours
		self.players = []
		self.tournee = tournee
		self.timeControl = timeControl
