#Luokka lisavaruste

from application import db

class Lisavaruste(db.Model):

    id = db.Column(db.Integer, primary_key=True) 

    nimi = db.Column(db.String(144), nullable=False)
 
    def __init__(self, nimi):
        self.nimi = nimi
  


