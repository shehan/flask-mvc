from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired("Please enter your email address."), Email('Invalid email format.')])
    password = PasswordField("Password", validators=[InputRequired("Please enter your password.")])
    submit = SubmitField("Submit")
