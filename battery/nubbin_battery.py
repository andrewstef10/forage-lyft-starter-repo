from abc import ABC

from car_components import Battery
from datetime import date

class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    # determines if the nubbin battery needs service
    def needs_service(self):
        #Nubbin batteries needs service once every 4 years
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return (service_threshold_date < self.current_date)
        
