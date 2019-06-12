#lomakkeen kasittelyyn tarvittava toiminnallisuus
#Eli lomakkeen nayttaminen ja kasittely

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User, Rooli
from application.auth.forms import LoginForm

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
                               error = "No such username or password")

    #jos kayttaja loytyy tulostetaan tieto tunnistamisesta ja palataan sovelluksen etusivulle
    #print("Käyttäjä " + user.name + " tunnistettiin")

    #kirjautumislomakkeen käsittelyyn kirjautuminen
    login_user(user)
    return redirect(url_for("index")) 


#uloskirjautumistoiminnallisuus
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))   
