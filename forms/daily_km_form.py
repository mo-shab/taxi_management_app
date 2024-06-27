from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class DailyKmForm(FlaskForm):
    km = IntegerField('Kilometers', validators=[DataRequired()])
    submit = SubmitField('Add Kilometers')