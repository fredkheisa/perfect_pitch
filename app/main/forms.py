from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class AddPitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    pitch = StringField("Go", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("pick-ups", "pick-ups"),("boring","boring")],validators = [Required()]
    )
    submit = SubmitField("Add pitch")