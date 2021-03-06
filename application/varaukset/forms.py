#sisaltaa varausten kasittelyyn tarvittavan lomakkeen

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators
from application.huoneet.models import Huone

class VarausForm(FlaskForm):

    varausviikko = IntegerField("Varausviikko", [validators.NumberRange(min=1, max=52, message="Viikkonumeron pitää olla 1-52")]) 
    huone_id = IntegerField("Huoneen id", [validators.NumberRange(min=1, max=1000, message="Huone_id pitää olla 1-1000.")])
    asiakas_id = IntegerField("Asiakkaan id", [validators.NumberRange(min=1, max=1000, message="Asiakas_id pitää olla 1-1000.")])
    hinta = IntegerField("Huoneen hinta", [validators.NumberRange(min=1, max=2000, message="Hinnan pitää olla 1-2000")])
    
    class Meta:
        csrf = False 
