from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired


TYPES = ["fire",
         "electric",
         "normal",
         "ghost",
         "psychic",
         "water",
         "bug",
         "dragon",
         "grass",
         "fighting",
         "ice",
         "flying",
         "poison",
         "ground",
         "rock",
         "steel"]


class PokemonForm(FlaskForm):
    number = IntegerField("number", validators=[DataRequired()])
    attack = IntegerField("attack", validators=[DataRequired()])
    defense = IntegerField("defense", validators=[DataRequired()])
    imageUrl = StringField("imageUrl", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    type = SelectField("type", validators=[DataRequired()], choices=TYPES)
    moves = StringField("moves", validators=[DataRequired()])