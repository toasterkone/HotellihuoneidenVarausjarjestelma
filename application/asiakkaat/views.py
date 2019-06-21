
#sisaltaa asiakkaiden kasittelyyn ja nakymien nayttamiseen liittyvat toiminnallisuudet

#uuden asiakkaan luominen asettaa myös käyttäjän luotavalle asiakkaalle. 

from application import app, db, login_required, login_manager
from flask import redirect, render_template, request, url_for
from application.asiakkaat.models import Asiakas
from application.asiakkaat.forms import AsiakasForm

from flask_login import current_user#, login_required 





#kuuntelee GET-tyyppisia pyyntoja polkuun /asiakkaat
@app.route("/asiakkaat/", methods=["GET"])
def asiakkaat_index():
    return render_template("asiakkaat/list.html", asiakkaat = Asiakas.query.all())


#nayttaa kayttajalle lomakkeen, jolla luodaan asiakkaita
@app.route("/asiakkaat/new/")
@login_required()
def asiakkaat_form():
    return render_template("asiakkaat/new.html", form = AsiakasForm())

#lisaa uuden asiakkaan pyynnossa lahetetyn lomakkeen perusteella
@app.route("/asiakkaat/", methods=["POST"])
@login_required()
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
@app.route("/asiakkaat/<asiakas_id>/muokkaa/", methods=["GET", "POST"])
@login_required()
def asiakkaat_update_tiedot(asiakas_id):
    #jos GET
    if request.method == "GET":

        asiakas = Asiakas.query.get(asiakas_id)
        form = AsiakasForm(obj=asiakas)   

        return render_template("asiakkaat/muokkaa.html", form=form, asiakas_id=asiakas_id)
    #jos POST
    form = AsiakasForm(request.form)
    asiakas = Asiakas.query.get(asiakas_id) 
      
    if not form.validate():
        return render_template("asiakkaat/muokkaa.html", form=form, asiakas_id=asiakas_id)

    asiakas.etunimi = form.etunimi.data
    asiakas.sukunimi = form.sukunimi.data
    asiakas.puhelinnumero = form.puhelinnumero.data
    asiakas.email = form.email.data


    db.session().commit()

    return redirect(url_for("asiakkaat_index"))


#asiakkaan poistaminen, vaatii kirjautumisen
@app.route("/asiakkaat/<asiakas_id>/delete", methods=["GET"])
@login_required() 
def asiakkaat_delete(asiakas_id):

    db.session.delete(Asiakas.query.get(asiakas_id))
    db.session().commit()

    return redirect(url_for("asiakkaat_index"))



