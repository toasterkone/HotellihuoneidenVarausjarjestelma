#Lomake-luokka = LoginForm



from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
#Lomake kirjautumiselle
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False


#nimi, username ja salasana minimi 2 ja maksimi 144 merkkia
#Lomake uudelle kayttajalle
class RekisteriForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144)])
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = StringField("Password", [validators.Length(min=2, max=144)])


    class Meta:
        csrf = False
