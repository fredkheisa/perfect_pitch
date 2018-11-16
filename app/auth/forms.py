from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField,ValidationError,BooleanField
from wtforms.validators import Required, EqualTo, Email
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [Required()])
    email = StringField("Email", validators = [Required(), Email()])
    password = PasswordField("Password", validators=[Required(), EqualTo("pass_confirm", message="Passwords do not match")])
    pass_confirm = PasswordField("Confirm password", validators = [Required()])
    submit = SubmitField("Register")

    def validate_username(self,data_field):
        if User.query.filter_by(name = data_field.data).first():
            raise ValidationError("username is already taken")


    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email")        

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[Required(),Email()])
    password = PasswordField("Password", validators = [Required()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")