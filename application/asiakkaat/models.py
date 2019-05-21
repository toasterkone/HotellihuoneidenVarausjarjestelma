from application import db

#Asiakas-luokka, tieto id, etu- ja sukunimi, email, puhnum
class Asiakas(db.Model):
    id = db.Column(db.Integer, primary_key=True)


    etunimi = db.Column(db.String(144), nullable=False)
    sukunimi = db.Column(db.String(144), nullable=False)
    puhelinnumero = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)

    

    def __init__(self, etunimi, sukunimi, puhelinnumero, email):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.puhelinnumero = puhelinnumero
        self.email = email

