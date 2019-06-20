
#sisaltaa varausten kasittelyyn ja nakymien nayttamiseen liittyvat toiminnallisuudet

#uuden varauksen luominen asettaa myös huoneen/asiakkaan luotavalle varaukselle. 

from application import app, db
from flask import redirect, render_template, request, url_for
#from application.asiakkaat.models import Asiakas
#from application.asiakkaat.forms import AsiakasForm

from application.varaukset.models import Varaus
from application.varaukset.forms import VarausForm

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
@app.route("/varaukset/", methods=["POST"])
@login_required
def varaukset_create():


    form = VarausForm(request.form)
    

    #jos virheelliset syotteet, naytetaan lomakesivu uudestaan
    if not form.validate():
        return render_template("varaukset/new.html", form = form)
    



    v = Varaus(form.varausviikko.data,form.hinta.data)


    #varaukselle asiakas_id
    v.asiakas_id = form.asiakas_id.data
    #varaukselle huone_id
    v.huone_id = form.huone_id.data
    #hinta haetaan huone_id:n perusteella
    #v.hinta = Huone.query.get(form.huone_id.data)
 

    #huoneelle varaus
    #v.asiakas_id = current_user.id

    #asiakkaalle varaus
    #v._id = current_user.id
  
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




