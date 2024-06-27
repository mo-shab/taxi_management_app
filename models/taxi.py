import json
from datetime import datetime

class Taxi:
    def __init__(self, number, immatriculation, total_km, next_maintenance, daily_km_log=None):
        self.number = number
        self.immatriculation = immatriculation
        self.total_km = total_km
        self.next_maintenance = next_maintenance
        self.daily_km_log = daily_km_log if daily_km_log is not None else []

    @classmethod
    def load_all(cls):
        with open('data/taxis.json', 'r') as f:
            data = json.load(f)
            return [cls(**taxi) for taxi in data]

    @classmethod
    def save_all(cls, taxis):
        with open('data/taxis.json', 'w') as f:
            json.dump([taxi.__dict__ for taxi in taxis], f)

    @classmethod
    def add_taxi(cls, taxi):
        taxis = cls.load_all()
        taxis.append(taxi)
        cls.save_all(taxis)

    @classmethod
    def get_taxi_by_number(cls, number):
        taxis = cls.load_all()
        for taxi in taxis:
            if taxi.number == number:
                return taxi
        return None

    @classmethod
    def delete_taxi(cls, number):
        taxis = cls.load_all()
        taxis = [taxi for taxi in taxis if taxi.number != number]
        cls.save_all(taxis)

    def update_taxi(self, immatriculation, total_km, next_maintenance):
        self.immatriculation = immatriculation
        self.total_km = total_km
        self.next_maintenance = next_maintenance

        taxis = self.load_all()
        for i, t in enumerate(taxis):
            if t.number == self.number:
                taxis[i] = self
                break
        self.save_all(taxis)

    def add_daily_km(self, km):
        today = datetime.now().strftime('%Y-%m-%d')
        self.daily_km_log.append({"date": today, "km": km})
        self.total_km += km

        taxis = self.load_all()
        for i, t in enumerate(taxis):
            if t.number == self.number:
                taxis[i] = self
                break
        self.save_all(taxis)
