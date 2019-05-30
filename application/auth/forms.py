#Lomake-luokka = LoginForm
#sisaltaa 2 kenttaa: kayttajatunnus, salasana

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False
