from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class Register(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=60)])
    password = PasswordField('Password', validator=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Confirm Password', validator=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired, Email(), Length(min=6, max=60)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')