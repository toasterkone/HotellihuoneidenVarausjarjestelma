#Luokka huone

from application import db

class Huone(db.Model):

    id = db.Column(db.Integer, primary_key=True) #Paa-avain

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    #attribuutteja
    huonenumero = db.Column(db.Integer, nullable=False)
    hinta = db.Column(db.Integer, nullable=False)
    tyyppi = db.Column(db.String(144), nullable=False)

    #jokaiseen huoneeseen liitetään huoneen varaus-tiedot
    varaukset = db.relationship("Varaus", backref='varaus2', lazy=True)
 
    def __init__(self, huonenumero, hinta, tyyppi):
        self.huonenumero = huonenumero
        self.hinta = hinta
        self.tyyppi = tyyppi


