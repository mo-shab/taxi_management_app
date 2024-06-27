from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DriverForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    id = StringField('ID', validators=[DataRequired()])
    license_id = StringField('License ID', validators=[DataRequired()])
    associated_taxi = StringField('Associated Taxi', validators=[DataRequired()])
    submit = SubmitField('Add Driver')
