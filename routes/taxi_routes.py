from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from models.taxi import Taxi
from forms.taxi_form import TaxiForm
from forms.daily_km_form import DailyKmForm

taxi_bp = Blueprint('taxi_bp', __name__)

@taxi_bp.route('/taxis', methods=['GET'])
def get_taxis():
    taxis = Taxi.load_all()
    return render_template('taxi_list.html', taxis=taxis)

@taxi_bp.route('/taxis/add', methods=['GET', 'POST'])
def add_taxi():
    form = TaxiForm()
    if form.validate_on_submit():
        taxi = Taxi(
            number=form.number.data,
            immatriculation=form.immatriculation.data,
            total_km=form.total_km.data,
            next_maintenance=form.next_maintenance.data
        )
        Taxi.add_taxi(taxi)
        flash('Taxi added successfully!', 'success')
        return redirect(url_for('taxi_bp.get_taxis'))
    return render_template('taxi_form.html', form=form)

@taxi_bp.route('/taxis/<number>', methods=['GET', 'POST'])
def get_taxi(number):
    taxi = Taxi.get_taxi_by_number(number)
    if taxi:
        form = DailyKmForm()
        if form.validate_on_submit():
            km = form.km.data
            taxi.add_daily_km(km)
            flash('Kilometers added successfully!', 'success')
            return redirect(url_for('taxi_bp.get_taxi', number=number))
        return render_template('taxi_detail.html', taxi=taxi, form=form)
    return jsonify({"error": "Taxi not found"}), 404

@taxi_bp.route('/taxis/<number>/edit', methods=['GET', 'POST'])
def edit_taxi(number):
    taxi = Taxi.get_taxi_by_number(number)
    if not taxi:
        return jsonify({"error": "Taxi not found"}), 404

    form = TaxiForm(obj=taxi)
    if form.validate_on_submit():
        taxi.update_taxi(
            immatriculation=form.immatriculation.data,
            total_km=form.total_km.data,
            next_maintenance=form.next_maintenance.data
        )
        flash('Taxi updated successfully!', 'success')
        return redirect(url_for('taxi_bp.get_taxi', number=number))
    return render_template('taxi_form.html', form=form)

@taxi_bp.route('/taxis/<number>/delete', methods=['POST'])
def delete_taxi(number):
    Taxi.delete_taxi(number)
    flash('Taxi deleted successfully!', 'success')
    return redirect(url_for('taxi_bp.get_taxis'))
