from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired(message="Enter a pet name")])
    species = StringField("Species", validators=[InputRequired(message="Enter a species"), AnyOf(values=["cat", "dog", "porcupine"], message="We only offer cats, dogs, or porcupines for adoption.")])
    photo_url = StringField("Pet Image URL", validators=[Optional(), URL(require_tld=True, message="Not a valid URL")])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30, message="Enter an age between 0 and 30")])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form to edit pet details."""

    photo_url = StringField("Pet Image URL", validators=[Optional(), URL(require_tld=True, message="Not a valid URL")])
    notes = StringField("Notes")
    available = BooleanField("Available to adopt?")