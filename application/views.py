from flask import render_template
from application import app

#tiedosto sisaltaa ohjeistuksen sovelluksen paasivulle paasemiseen

#Ohjeistaa Flaskia siten, etta jokainen juuripolkuun "/" saapuva pyynto johtaa kayttajalla index.html-tiedoston nayttamiseen

@app.route("/")
def index():
    return render_template("index.html")
