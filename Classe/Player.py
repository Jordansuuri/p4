
class Player:
    def __init__(self, nom, prenom, sexe, date, ranking=0):
        """initialise le nom et l'age du joueur"""
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date = date
        self.ranking = ranking


    def serialise(self):
        """Transforme l'objet en format json pour tinyDB"""
        return {'nom':self.nom,'prenom':self.prenom,'date':self.date,'sexe':self.sexe,'ranking':self.ranking}

    def set_ranking(self, nouveau_ranking):
        self.ranking = nouveau_ranking
