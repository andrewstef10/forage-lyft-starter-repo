from abc import ABC, abstractmethod

#this file contains abstract classes for differnt car components

class Engine(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Battery(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Tire(ABC):
    # tire_wear_arr is an array that contains 4 floats
    # with values between zero and 1
    def __init__(self, tire_wear_arr) -> None:
        self.tire_wear_arr = tire_wear_arr

    def needs_service(self) -> bool:
        pass





