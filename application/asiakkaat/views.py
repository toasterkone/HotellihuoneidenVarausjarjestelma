
#sisaltaa asiakkaiden kasittelyyn ja nakymien nayttamiseen liittyvat toiminnallisuudet

#uuden asiakkaan luominen asettaa myös käyttäjän luotavalle asiakkaalle. 

from application import app, db
from flask import redirect, render_template, request, url_for
from application.asiakkaat.models import Asiakas
from application.asiakkaat.forms import AsiakasForm

from flask_login import login_required, current_user





#kuuntelee GET-tyyppisia pyyntoja polkuun /asiakkaat
@app.route("/asiakkaat/", methods=["GET"])
def asiakkaat_index():
    return render_template("asiakkaat/list.html", asiakkaat = Asiakas.query.all())


#nayttaa kayttajalle lomakkeen, jolla luodaan asiakkaita
@app.route("/asiakkaat/new/")
@login_required
def asiakkaat_form():
    return render_template("asiakkaat/new.html", form = AsiakasForm())

#lisaa uuden asiakkaan pyynnossa lahetetyn lomakkeen perusteella
@app.route("/asiakkaat/", methods=["POST"])
@login_required
def asiakkaat_create():

    #Asiakas-oliolle haetaan tekstikentista attribuutit
    #a = Asiakas(request.form.get("etunimi"), request.form.get("sukunimi"), request.form.get("puhelinnumero"), request.form.get("email"))

  
    form = AsiakasForm(request.form)
    

    #jos virheelliset syotteet, naytetaan lomakesivu uudestaan
    if not form.validate():
        return render_template("asiakkaat/new.html", form = form)
    

    a = Asiakas(form.etunimi.data,form.sukunimi.data,form.puhelinnumero.data,form.email.data)
    
    #kayttajalle asiakas
    a.account_id = current_user.id
  
    db.session().add(a)
    db.session().commit()


    return redirect(url_for("asiakkaat_index"))









#metodi paivittaa kaikki tiedot, jotka halutaan muuttaa
@app.route("/asiakkaat/<asiakas_id>/", methods=["POST"])
def asiakkaat_update_tiedot(asiakas_id):

    a = Asiakas.query.get(asiakas_id)

    if request.form.get("sukunimi") is not None:
        a.sukunimi = request.form.get("sukunimi") #hakee tekstikenttaan syotetyn merkkijonon
    if request.form.get("etunimi") is not None:

        a.etunimi = request.form.get("etunimi") #hakee tekstikenttaan syotetyn merkkijonon

    if request.form.get("email") is not None:

        a.email = request.form.get("email") #hakee tekstikenttaan syotetyn merkkijonon

    if request.form.get("puhelinnumero") is not None:
        a.puhelinnumero = request.form.get("puhelinnumero") #hakee tekstikenttaan syotetyn merkkijonon

  
    db.session().commit()
  
    return redirect(url_for("asiakkaat_index"))


#asiakkaan poistaminen, vaatii kirjautumisen
@app.route("/asiakkaat/<asiakas_id>/delete", methods=["GET"])
@login_required 
def asiakkaat_delete(asiakas_id):

    db.session.delete(Asiakas.query.get(asiakas_id))
    db.session().commit()

    return redirect(url_for("asiakkaat_index"))



