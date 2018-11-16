from ..models import User,Pitch,Comment
from .forms import AddPitchForm
from . import main
from flask import render_template

@main.route("/<uname>/add/pitch", methods = ["GET","POST"])
def index(uname):
    form = AddPitchForm()
    title = "Add Pitch"
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data 
        user = User.query.filter_by(name = uname).first()
        new_pitch = Pitch(title = title, content = pitch, category = category,user = user)
        new_pitch.save_pitch()  
        pitches = Pitch.query.all()
        return render_template("posted.html", pitches = pitches)
    return render_template("index.html",form = form, title = title)

