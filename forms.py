from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """form to add a pet to app"""
    name = StringField('Pet Name')
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Image Source', validators=[URL(message='Please enter a valid url'), Optional()])
    age = FloatField('Age', validators=[NumberRange(min=0, max=30, message='Choose an age between 0 and 30')])
    notes = StringField('Additional Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    """form to edit a pet on app"""
    photo_url = StringField('Image Source', validators=[URL(message='Please enter a valid url'), Optional()])
    notes = StringField('Additional Notes', validators=[Optional()])
    available = BooleanField('Available?')