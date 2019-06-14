#Varaus-luokka

from application import db



#Varaus-tauluun liittyy aina asiakas- ja huone-taulu
class Varaus(db.Model):

    id = db.Column(db.Integer, primary_key=True) #Paa-avain



    #attribuutteja
    varausviikko = db.Column(db.Integer, nullable=False)
    hinta = db.Column(db.Integer, nullable=False)

    #viiteavain viittaa asiakas-tauluun
    #asiakas_id = db.Column(db.Integer, db.ForeignKey('asiakas.id'),primary_key=True)                          

    #viiteavain viittaa huone-tauluun
    #huone_id = db.Column(db.Integer, db.ForeignKey('huone.id'),primary_key=True)


    #viiteavain viittaa asiakas-tauluun
    asiakas_id = db.Column(db.Integer, db.ForeignKey('asiakas.id'),nullable=True)

    #viiteavain viittaa huone-tauluun
    huone_id = db.Column(db.Integer, db.ForeignKey('huone.id'),nullable=False)
    

    def __init__(self, varausviikko, hinta):
        self.varausviikko = varausviikko
        self.hinta = hinta






