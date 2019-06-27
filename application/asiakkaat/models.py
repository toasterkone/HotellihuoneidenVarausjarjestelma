from application import db

#Asiakas-luokka
#Asiakas-tauluun liittyy aina account(käyttäjä)-taulu
class Asiakas(db.Model):

    id = db.Column(db.Integer, primary_key=True) #Paa-avain
    #attribuutteja
    etunimi = db.Column(db.String(144), nullable=False)
    sukunimi = db.Column(db.String(144), nullable=False)
    puhelinnumero = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)

    #viiteavain viittaa account-tauluun
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    #jokaiseen asiakkaaseen liitetään asiakkaan varaus-tiedot
    varaukset = db.relationship("Varaus", backref='varaus1', lazy=True)
  
    def __init__(self, etunimi, sukunimi, puhelinnumero, email):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.puhelinnumero = puhelinnumero
        self.email = email

