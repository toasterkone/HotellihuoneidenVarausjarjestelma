#lomakkeen kasittelyyn tarvittava toiminnallisuus
#Eli lomakkeen nayttaminen ja kasittely

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User, Rooli
from application.auth.forms import LoginForm, RekisteriForm

#kayttaja hakee lomaketta -> naytetaan lomake kayttajalle
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    #jos kayttajaa ei loydy -> nayta lomake uudestaan + virheviesti
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjänimi tai salasana virheellinen.")

    #jos kayttaja loytyy tulostetaan tieto tunnistamisesta ja palataan sovelluksen etusivulle
    #print("Käyttäjä " + user.name + " tunnistettiin")

    #kirjautumislomakkeen käsittelyyn kirjautuminen
    login_user(user)
    return redirect(url_for("index")) 




#rekisteroytymiselle toiminnallisuus
@app.route("/auth/uusi_kayttaja", methods=["GET", "POST"])
def auth_rekisteroidy():

    if request.method == "GET":
        return render_template("auth/uusi_kayttaja.html", form=RekisteriForm())

    form = RekisteriForm(request.form)

    #jos ei oikeita syotteita -> palautaa samalle sivulle
    if not form.validate():
        return render_template("auth/uusi_kayttaja.html", form = form)

    #Luodaan uusi kayttaja, haetaan tiedot lomakkeesta
    kayttaja = User(form.name.data, form.username.data, form.password.data)
    #rooli on automaattisesti kayttaja eika ADMIN    
    #kayttaja.rooli = Rooli.query.get(2)
    kayttaja.rooli_id = 2 

    
    db.session().add(kayttaja)
    db.session().commit()

    #lopuksi ohjaa kirjautumaan
    return redirect(url_for("auth_login"))





#uloskirjautumistoiminnallisuus
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))   
