#sisaltaa toiminnallisuudet huoneiden kasittelyyn
# ja nakymien nayttamiseen liittyvat toiminnallisuudet
#toiminnallisuudet lisaa ja listaa


#me ei aluta kayttajaa huoneelle, koska ei oleellista
#ei huone-tauluun kayttaja_id:ta
#vai halutaanko?

from application import app, db
from flask import redirect, render_template, request, url_for
from application.huoneet.models import Huone
from application.huoneet.forms import HuoneForm

from flask_login import login_required, current_user





#kuuntelee GET-tyyppisia pyyntoja polkuun /huoneet
@app.route("/huoneet/", methods=["GET"])
def huoneet_index():
    return render_template("huoneet/list.html", huoneet = Huone.query.all())


#nayttaa kayttajalle lomakkeen, jolla luodaan huoneita
@app.route("/huoneet/new/")
@login_required
def huoneet_form():
    return render_template("huoneet/new.html", form = HuoneForm())

#lisaa uuden huoneen pyynnossa lahetetyn lomakkeen perusteella
@app.route("/huoneet/", methods=["POST"])
@login_required
def huoneet_create():



  
    form = HuoneForm(request.form)
    

    #jos virheelliset syotteet, naytetaan lomakesivu uudestaan
    if not form.validate():
        return render_template("huoneet/new.html", form = form)
    

    h = Huone(form.huonenumero.data,form.hinta.data,form.tyyppi.data)
    
    #huoneelle varaus (liitostaulu
    #h.varaus_id = current_user.id ??
  
    db.session().add(h)
    db.session().commit()


    return redirect(url_for("huoneet_index"))






