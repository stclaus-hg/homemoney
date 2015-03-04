from flask_wtf import Form
from flask_wtf.html5 import EmailField
from wtforms.validators import Email, DataRequired, Length
from wtforms import PasswordField, StringField


class ItemForm(Form):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])


class ItemRemove(Form):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])


class GroupForm(Form):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
