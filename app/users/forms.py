from app import bcrypt
from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms.validators import Email, DataRequired, ValidationError, InputRequired
from wtforms import PasswordField, StringField


class LoginForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ProfileForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])

    current_password = PasswordField('Current Password')
    password = PasswordField('New Password')
    retype_password = PasswordField('Retype Password')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ProfileForm, self).__init__(*args, **kwargs)

    def validate_current_password(self, field):
        if not field.data and self.password.data:
            raise ValidationError('Please input current password')

        if field.data and not bcrypt.check_password_hash(self.user.password, field.data):
            raise ValidationError('Wrong password')

    def validate_password(self, field):
        if self.current_password.data and not field.data:
            raise ValidationError('This field is required.')

        if field.data and field.data != self.retype_password.data:
            raise ValidationError('Passwords must match')