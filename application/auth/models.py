#Kayttaja-luokka, nimetty account-luokaksi
#kayttajalla tunnus, tieto luomisesta/paivittamisesta nimi, kayttajanimi, salasana

#käyttäjälle on metodit get_id, is_active, is_anonymous sekä is_authenticated.

#sisaltaa myos rooli-luokan

from application import db, app, login_required

from sqlalchemy.sql import text



class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    ##jokaiseen käyttäjään liitetään käyttäjän asiakas-tiedot
    asiakkaat = db.relationship("Asiakas", backref='account', lazy=True)

    #kayttajalla on FK rooli_id
    rooli_id = db.Column(db.Integer, db.ForeignKey("rooli.id"), nullable=True)
    rooli = db.relationship("Rooli")

    def __init__(self, name, username, password): #ns. konstruktori(javassa)
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True



 




    #metodi, palauttaa kayttajat, joilla ei yhtaan asiakasta
    @staticmethod
    def etsi_kayttajat_ilman_asiakkaita():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Asiakas ON Asiakas.account_id = Account.id"
                     " WHERE Asiakas.id IS NULL"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Asiakas.id) = 0")

        res = db.engine.execute(stmt)

        #tuloksista luodaan lista, joka sisaltaa jokaiseen tulosriviin liittyvan
        #hajautustaulun
        response = []
        for row in res:
            response.append({"id":row[0],"name":row[1]})

        return response


#Rooli-luokka, jolla attribuutit id ja nimi
class Rooli(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(32), nullable=False)
    
    def __init__(self, nimi):
        self.nimi = nimi




