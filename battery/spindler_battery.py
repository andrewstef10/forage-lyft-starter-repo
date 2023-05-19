from abc import ABC

from car_components import Battery
from datetime import date

class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    # determines if the spinder battery needs service
    def needs_service(self):
        #Spindler batteries needs service once every 2 years
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return (service_threshold_date < self.current_date)