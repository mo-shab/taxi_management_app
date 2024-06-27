from flask import Blueprint, render_template
from models.taxi import Taxi
from models.driver import Driver

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/')
def dashboard():
    taxis = Taxi.load_all()
    drivers = Driver.load_all()
    return render_template('dashboard.html', taxis=taxis, drivers=drivers)