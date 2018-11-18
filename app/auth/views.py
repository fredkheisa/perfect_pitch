from . import auth
from .forms import RegistrationForm,LoginForm
from app.models import User
from flask import render_template,url_for,redirect,flash
from flask_login import login_user,logout_user
from app.email import create_mail

@auth.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    title = 'Pitch Perfect- Register'
    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        pass_input = form.password.data
        profile_pic = "photos/default.png"
        bio = "User has no bio"
        new_user = User(name = name, email = email, password = pass_input,profile_pic = profile_pic, bio = bio)
        new_user.save_user()
        create_mail("Welcome","email/emai",new_user.email,name = name)
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html",form = form,title = title)

    
@auth.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    title = "Pitch Perfect - Login"
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        remember = form.remember_me.data

        user = User.query.filter_by(email = user_email).first()

        if user is not None and user.verify_pass(user_password):
            login_user(user,remember)
            flash("Welcome to Pitch Perfect")
            return redirect(url_for("main.index", user = user))
        flash("Invalid username or pasword")
    return render_template("auth/login.html",form = form,title = title)


@auth.route("/logout")
def logout():
    logout_user()
    flash("You have successfully logged out")
    return redirect(url_for("main.index"))