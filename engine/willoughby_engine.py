from abc import ABC

from car_components import Engine


class WilloughbyEngine(Engine, ABC):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    # determines if the Willoughby engine needs service
    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > 60000
