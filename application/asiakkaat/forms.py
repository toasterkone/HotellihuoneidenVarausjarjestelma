#sisaltaa asiakkaiden kasittelyyn tarvittavat lomakkeet


from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

#etunimi minimi 2 merkkia
#sukunimi minimi 2 merkkia
#puhelinnumero minimi 5 merkkia
#email minimi 3 merkkia

class AsiakasForm(FlaskForm):
    #Tekstikentat asiakkaan etu- ja sukunimea, puhelinnumeroa, emailia varten
    
    etunimi = StringField("Asiakas etunimi", [validators.Length(min=2, max=144, message="Etunimen pituuden pitää olla 2-144 merkkiä.")])
    sukunimi = StringField("Asiakas sukunimi", [validators.Length(min=2, max=144, message="Sukunimen pituuden pitää olla 2-144 merkkiä.")])
    puhelinnumero = StringField("Asiakas puhelinnumero", [validators.Length(min=5, max=144, message="Puhelinnumeron pituuden pitää olla 5-144 merkkiä.")])
    email = StringField("Asiakas email", [validators.Length(min=3, max=144, message="Sähköpostin pituuden pitää olla 3-144 merkkiä.")])
    
 
    class Meta:
        csrf = False #turvautuminen cross-site request forgery -hyökkäyksiä vastaan kytketään pois päältä. 
