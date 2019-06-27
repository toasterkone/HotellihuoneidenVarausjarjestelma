#Kirjautumiselle ja rekisteröitymiselle lomakkeet

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
#Lomake kirjautumiselle
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

#Lomake uudelle kayttajalle
class RekisteriForm(FlaskForm):
    name = StringField("Kokonimi (etunimi sukunimi)", [validators.Length(min=2, max=144, message="Kokonimen pituuden pitää olla 2-144 merkkiä.")])
    username = StringField("Käyttäjänimi", [validators.Length(min=2, max=144, message="Käyttäjänimen pituuden pitää olla 2-144 merkkiä.")])
    password = StringField("Salasana", [validators.equal_to('vahvista', message='Salasanat pitää täsmätä'),validators.Length(min=2, max=144, message="Salasanan pituuden pitää olla 2-144 merkkiä.")])
    vahvista = StringField("Toista salasana")

    class Meta:
        csrf = False
