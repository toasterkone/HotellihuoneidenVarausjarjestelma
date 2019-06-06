#sisaltaa huoneiden kasittelyyn tarvittavat lomakkeet


from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators

#huonenumero minimi numero 1
#hinta minimi numero 1
#tyyppi minimi 3 merkkia


class HuoneForm(FlaskForm):
    #Tekstikentat huoneen numeroa, hintaa, tyyppia varten
    huonenumero = IntegerField("Huonenumero", [validators.NumberRange(min=1)]) #vahintaan 2 merkkia
    hinta = IntegerField("Huone hinta", [validators.NumberRange(min=1)])
    tyyppi = StringField("Huone tyyppi", [validators.Length(min=3)])

    
 
    class Meta:
        csrf = False #turvautuminen cross-site request forgery -hyökkäyksiä vastaan kytketään pois päältä. 
