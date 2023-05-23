from abc import ABC
from car_components import Tire

class CarriganTire(Tire, ABC):
    def __init__(self, tire_wear_arr) -> None:
        super().__init__(tire_wear_arr)

    #carrigan tires need service if one or more of the tire wear values are
    #greater than or equal 0.9
    def needs_service(self) -> bool:
        for i in self.tire_wear_arr:
            if (i >= 0.9):
                return True
            
        return False