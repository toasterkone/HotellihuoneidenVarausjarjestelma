from flask import render_template
from application import app
from application.auth.models import User
from application.asiakkaat.models import Asiakas
from application.huoneet.models import Huone
from application.varaukset.models import Varaus
from application.lisavarusteet.models import Lisavaruste

#tiedosto sisaltaa ohjeistuksen sovelluksen paasivulle paasemiseen

#Ohjeistaa Flaskia siten, etta jokainen juuripolkuun "/" saapuva pyynto johtaa kayttajalla index.html-tiedoston nayttamiseen

#metodikutsun "etsi_kayttajat_ilman_asiakkaita()" palauttama lista lisataan
#osaksi paasivun luomista

@app.route("/")
def index():
    return render_template("index.html",needs_asiakkaita=User.etsi_kayttajat_ilman_asiakkaita())
    #return render_template("index.html")
