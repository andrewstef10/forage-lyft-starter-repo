from abc import ABC
from car_components import Tire

class CarriganTire(Tire, ABC):
    def __init__(self, tire_wear_arr) -> None:
        super().__init__(tire_wear_arr)

    #octoprime tires need service when the sum of the values in the tire wear
    #array are greater than or equal to 3
    def needs_service(self) -> bool:
        sum = 0
        for i in self.tire_wear_arr:
            sum += i

        return (sum >= 3)