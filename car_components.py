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




