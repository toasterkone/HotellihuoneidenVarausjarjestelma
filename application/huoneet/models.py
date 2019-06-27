#Luokka huone

from application import db
from application.auth import models

#Liitostaulu huonelisavaruste
lisavarusteet = db.Table('huonelisavaruste',db.Column('huone_id', db.Integer,db.ForeignKey('huone.id'), primary_key=True),db.Column('lisavaruste_id', db.Integer,db.ForeignKey('lisavaruste.id'), primary_key=True))

class Huone(db.Model):

    id = db.Column(db.Integer, primary_key=True) 

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    #attribuutteja
    huonenumero = db.Column(db.Integer, nullable=False)
    hinta = db.Column(db.Integer, nullable=False)
    tyyppi = db.Column(db.String(144), nullable=False)

    #jokaiseen huoneeseen liitetään huoneen varaus-tiedot
    varaukset = db.relationship("Varaus", backref='varaus2', lazy=True)

    #Huoneella lisavarusteita
    lisavarusteet = db.relationship('Lisavaruste', secondary=lisavarusteet, lazy='subquery',backref=db.backref('huoneet', lazy=True))
 
    def __init__(self, huonenumero, hinta, tyyppi):
        self.huonenumero = huonenumero
        self.hinta = hinta
        self.tyyppi = tyyppi


