
#sisaltaa varausten kasittelyyn ja nakymien nayttamiseen liittyvat toiminnallisuudet

#uuden varauksen luominen asettaa myös huoneen/asiakkaan luotavalle varaukselle. 

from application import app, db
from flask import redirect, render_template, request, url_for
#from application.asiakkaat.models import Asiakas
#from application.asiakkaat.forms import AsiakasForm

from application.varaukset.models import Varaus
from application.varaukset.forms import VarausForm

from application.huoneet.models import Huone
from application.asiakkaat.models import Asiakas

from flask_login import login_required, current_user





#kuuntelee GET-tyyppisia pyyntoja polkuun /varaukset
#varausten listaaminen
@app.route("/varaukset/", methods=["GET"])
def varaukset_index():
    return render_template("varaukset/list.html", varaukset = Varaus.query.all())


#nayttaa kayttajalle lomakkeen, jolla luodaan varauksia
@app.route("/varaukset/new/")
@login_required
def varaukset_form():
    return render_template("varaukset/new.html", form = VarausForm())

#lisaa uuden varauksen pyynnossa lahetetyn lomakkeen perusteella
@app.route("/varaukset/", methods = ["GET", "POST"])
@login_required
def varaukset_create():
    #syöta huone_id, asiakas_id, viikkonro, hinta
    if request.method == "GET":
        return render_template("varaukset/new.html", form = VarausForm())

    form = VarausForm(request.form)

    #jos virheelliset syotteet, naytetaan lomakesivu uudestaan
    if not form.validate():
        return render_template("varaukset/new.html", form = form)

    #onko huone olemassa
    olemassaolevaHuone = Huone.query.filter_by(id=form.huone_id.data).first()
    if not olemassaolevaHuone:
        return render_template("varaukset/new.html", form=form, error = "Huonetta ei ole olemassa.")  
    
    #matchaako huone ja hinta
    huone = Huone.query.filter_by(hinta=form.hinta.data,id=form.huone_id.data).first()
    if not huone:
        return render_template("varaukset/new.html", form=form, error = "Huoneen hinta ja id eivät vastaa.")

    #onko huone varattu jo varausviikkona
    vanhaVaraus = Varaus.query.filter_by(varausviikko=form.varausviikko.data, huone_id=form.huone_id.data).first()
    if vanhaVaraus:
        return render_template("varaukset/new.html", form=form, error = "Huone on jo varattuna haluttuna viikkona.") 

    #onko asiakas olemassa
    olemassaolevaAsiakas = Asiakas.query.filter_by(id=form.asiakas_id.data).first()
    if not olemassaolevaAsiakas:
        return render_template("varaukset/new.html", form=form, error = "Asiakasta ei ole olemassa.")      
   
    #jos oikeat tiedot
    v = Varaus(form.varausviikko.data,form.hinta.data)
    v.asiakas_id = form.asiakas_id.data
    v.huone_id = form.huone_id.data

    db.session().add(v)
    db.session().commit()

    return redirect(url_for("varaukset_index"))

#varauksen poistaminen, vaatii kirjautumisen
@app.route("/varaukset/<varaus_id>/delete", methods=["GET"])
@login_required 
def varaukset_poista(varaus_id):

    db.session.delete(Varaus.query.get(varaus_id))
    db.session().commit()

    return redirect(url_for("varaukset_index"))




