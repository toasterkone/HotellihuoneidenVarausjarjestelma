#sisältämään asiakkaiden käsittelyyn ja näkymien näyttämiseen liittyvät toiminnallisuudet. 

from application import app, db
from flask import redirect, render_template, request, url_for
from application.asiakkaat.models import Asiakas

#kuuntelee GET-tyyppisia pyyntoja polkuun /asiakkaat
@app.route("/asiakkaat", methods=["GET"])
def asiakkaat_index():
    return render_template("asiakkaat/list.html", asiakkaat = Asiakas.query.all())


#nayttaa kayttajalle lomakkeen, jolla luodaan asiakkaita
@app.route("/asiakkaat/new/")
def asiakkaat_form():
    return render_template("asiakkaat/new.html")

#lisaa uuden asiakkaan pyynnossa lahetetyn lomakkeen perusteella
@app.route("/asiakkaat/", methods=["POST"])
def asiakkaat_create():
    #print(request.form.get("etunimi")) #asetetaan etunimi
    #print(request.form.get("sukunimi")) #asetetaan sukunimi
    a = Asiakas(request.form.get("etunimi"), request.form.get("sukunimi"), request.form.get("puhelinnumero"), request.form.get("email"))

    db.session().add(a)
    db.session().commit()  

    return redirect(url_for("asiakkaat_index"))
