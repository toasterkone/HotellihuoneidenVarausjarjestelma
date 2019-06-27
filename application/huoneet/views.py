#sisaltaa toiminnallisuudet huoneiden kasittelyyn

from application import app, db, login_required #login omasta sovelluksesta

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.huoneet.models import Huone
from application.huoneet.forms import HuoneForm

#kuuntelee GET-tyyppisia pyyntoja polkuun /huoneet
@app.route("/huoneet/", methods=["GET"])
def huoneet_index():
    return render_template("huoneet/list.html", huoneet = Huone.query.all())

@app.route("/huoneet/new/")
@login_required(rooli="ADMIN")
def huoneet_form():
    return render_template("huoneet/new.html", form = HuoneForm())

#lisaa uuden huoneen pyynnossa lahetetyn lomakkeen perusteella
@app.route("/huoneet/", methods=["POST"])
@login_required(rooli="ADMIN")
def huoneet_create():
  
    form = HuoneForm(request.form)
  
    #jos virheelliset syotteet, naytetaan lomakesivu uudestaan
    if not form.validate():
        return render_template("huoneet/new.html", form = form)
   
    h = Huone(form.huonenumero.data,form.hinta.data,form.tyyppi.data)   

    db.session().add(h)
    db.session().commit()

    return redirect(url_for("huoneet_index"))






