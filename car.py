from abc import ABC
from car_components import Engine
from car_components import Battery

# creates a car object
class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    # determines if the car needs to be serviced
    def needs_service(self) -> bool:
        return ( self.engine.needs_service() or self.battery.needs_service() )
    

