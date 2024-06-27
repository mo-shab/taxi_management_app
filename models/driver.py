import json
import os

DATA_FILE = 'data/drivers.json'

class Driver:
    def __init__(self, name, id, license_id, associated_taxi):
        self.name = name
        self.id = id
        self.license_id = license_id
        self.associated_taxi = associated_taxi

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @staticmethod
    def load_all():
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return [Driver.from_dict(driver) for driver in data]

    @staticmethod
    def save_all(drivers):
        with open(DATA_FILE, 'w') as f:
            json.dump([driver.to_dict() for driver in drivers], f)

    @staticmethod
    def get_driver_by_id(driver_id):
        drivers = Driver.load_all()
        for driver in drivers:
            if driver.id == driver_id:
                return driver
        return None

    @staticmethod
    def add_driver(driver):
        drivers = Driver.load_all()
        drivers.append(driver)
        Driver.save_all(drivers)

    @staticmethod
    def update_driver(updated_driver):
        drivers = Driver.load_all()
        for i, driver in enumerate(drivers):
            if driver.id == updated_driver.id:
                drivers[i] = updated_driver
                break
        Driver.save_all(drivers)

    @staticmethod
    def delete_driver(driver_id):
        drivers = Driver.load_all()
        drivers = [driver for driver in drivers if driver.id != driver_id]
        Driver.save_all(drivers)
