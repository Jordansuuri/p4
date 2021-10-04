from Class.tinydb import TinyDB

class Tournament:
	"""initialise le nom, l'emplacement et la date du tournoi"""
	def __init__(self, name, location, date, tours = 4):
		self.name = name
		self.location = location
		self.date = date
		self.tours = tours
		self.players = []
		#la liste des tours : qui gagne qui perd#
		#ajout de la liste des joueurs#

