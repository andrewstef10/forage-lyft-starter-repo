from car_components import Engine
from car_components import Battery
from car_components import Tire

# creates a car object
class Car():
    def __init__(self, engine: Engine, battery: Battery, tires: Tire):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    # determines if the car needs to be serviced
    def needs_service(self) -> bool:
        return ( self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service())
    

