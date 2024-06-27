from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from models.driver import Driver
from models.taxi import Taxi
from forms.driver_form import DriverForm

driver_bp = Blueprint('driver_bp', __name__)

@driver_bp.route('/drivers', methods=['GET'])
def get_drivers():
    drivers = Driver.load_all()
    return render_template('driver_list.html', drivers=drivers)

@driver_bp.route('/drivers/add', methods=['GET', 'POST'])
def add_driver():
    form = DriverForm()
    if form.validate_on_submit():
        driver = Driver(
            name=form.name.data,
            id=form.id.data,
            license_id=form.license_id.data,
            associated_taxi=form.associated_taxi.data
        )
        Driver.add_driver(driver)
        flash('Driver added successfully!', 'success')
        return redirect(url_for('driver_bp.get_drivers'))
    return render_template('driver_form.html', form=form)

@driver_bp.route('/drivers/<driver_id>', methods=['GET', 'POST'])
def get_driver(driver_id):
    driver = Driver.get_driver_by_id(driver_id)
    taxi = Taxi.get_taxi_by_number(driver.associated_taxi)
    return render_template('driver_detail.html', driver=driver, taxi=taxi)

