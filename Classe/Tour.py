class Tour:
    def __init__(self, idtournoi, nom, match1, match2, match3, match4):
        self.idtournoi = idtournoi
        self.nom = nom
        self.match1 = match1
        self.match2 = match2
        self.match3 = match3
        self.match4 = match4

    def serialise(self):
        return { 'idtournoi':self.idtournoi, 'nom': self.nom, 'match1': self.match1, 'match2': self.match2, 'match3': self.match3, 'match4': self.match4}