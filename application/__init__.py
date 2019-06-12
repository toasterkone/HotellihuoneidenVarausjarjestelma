# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///asiakkaat.db"    
    app.config["SQLALCHEMY_ECHO"] = True

# Käytetään asiakkaat.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa

#muutin kommentiksi osa3
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///asiakkaat.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
#app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)



#OSA5
# kirjautuminen toiminnallisuus 1.
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
#login_manager.setup_app(app)
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


# roolit login_required:ssa
from functools import wraps

def login_required(rooli="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):


            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if rooli != "ANY":
                unauthorized = True
                
                user_rooli = current_user.rooli.nimi
                
                if user_rooli == rooli:
                    unauthorized = False


            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper





# Luetaan kansiosta application tiedoston views sisältö
from application import views

#jotta Asiakas-luokka on kaytossa
from application.asiakkaat import models
from application.asiakkaat import views

#account-luokka kayttoon
from application.auth import models
from application.auth import views

#huone-luokka kayttoon
from application.huoneet import models
from application.huoneet import views

#kirjautuminen 2.
from application.auth.models import User, Rooli









#load_user lataa tietokannasta käyttäjän avaimen perusteella. 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
try: 
    db.create_all()




except:
    pass


