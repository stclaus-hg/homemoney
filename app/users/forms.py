from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms.validators import Email, DataRequired
from wtforms import PasswordField


class LoginForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])