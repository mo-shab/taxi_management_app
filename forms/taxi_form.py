from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class TaxiForm(FlaskForm):
    number = StringField('Number', validators=[DataRequired()])
    immatriculation = StringField('Immatriculation', validators=[DataRequired()])
    total_km = IntegerField('Total KM', validators=[DataRequired()])
    next_maintenance = StringField('Next Maintenance Appointment', validators=[DataRequired()])
    submit = SubmitField('Add Taxi')
