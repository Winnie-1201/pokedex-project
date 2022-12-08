from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Pokemon, Item

class ItemForm(FlaskForm):
    happiness = IntegerField("happiness", validators=[DataRequired()])
    image_url = StringField("image_url", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    price = IntegerField("price", validators=[DataRequired()])
    

