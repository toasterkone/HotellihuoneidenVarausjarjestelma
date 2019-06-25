#sisaltaa huoneiden kasittelyyn tarvittavan lomakkeen

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators

class HuoneForm(FlaskForm):
    #Tekstikentat huoneen numeroa, hintaa, tyyppia varten
    huonenumero = IntegerField("Huonenumero", [validators.NumberRange(min=1, max=1000, message="Huonenumeron oltava väliltä 1-1000")]) 
    hinta = IntegerField("Huone hinta", [validators.NumberRange(min=1, max=2000, message="Hinnan oltava väliltä 1-2000")]) 
    tyyppi = StringField("Huone tyyppi", [validators.Length(min=3, max=144, message="Huoneen tyypin pituuden pitää olla 3-144 merkkiä.")]) 

    class Meta:
        csrf = False #turvautuminen cross-site request forgery -hyökkäyksiä vastaan kytketään pois päältä. 
