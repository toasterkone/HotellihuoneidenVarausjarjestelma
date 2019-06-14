#sisaltaa varausten kasittelyyn tarvittavat lomakkeet


from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

from application.huoneet.models import Huone





class VarausForm(FlaskForm):
    #tarvitsee syöttää varausviikko, huone_id, asiakas_id ja hinta
    varausviikko = IntegerField("Varausviikko", [validators.NumberRange(min=1, max=52)]) #vahintaan viikko 1, enintaan viikko 52
    huone_id = IntegerField("Huoneen id", [validators.NumberRange(min=1)])
    asiakas_id = IntegerField("Asiakkaan id", [validators.NumberRange(min=1)])
    hinta = IntegerField("Huoneen hinta", [validators.NumberRange(min=1)])
    

    #hinta = IntegerField("Huoneen hinta", [validators.equal_to('tarkistusHinta', message='Syota oikea hinta')])


    #tarkistetaan, että syötetty huoneen hinta vastaa oikeaa hintaa

    #h = Huone.query.filter_by(id=huone_id).first()
    #tarkistusHinta = h.hinta

    
 
    class Meta:
        csrf = False #turvautuminen cross-site request forgery -hyökkäyksiä vastaan kytketään pois päältä. 
