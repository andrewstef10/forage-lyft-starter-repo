from car import Car

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

from datetime import date

# contians functions to create differnt model cars
class CarFactory():

    # creates and returns a calliope Car
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_arr) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear_arr)
        calliope = Car(engine, battery, tires)
        return calliope
    
    # creates and returns a gilssade Car
    @staticmethod
    def create_gilssade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_arr) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear_arr)
        gilssade = Car(engine, battery, tires)
        return gilssade
    
    # creates and returns a palindrome Car
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear_arr):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear_arr)
        palindrome = Car(engine, battery, tires)
        return palindrome
    
    # creates and returns a rorschach Car
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_arr) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_wear_arr)
        rorschach = Car(engine, battery, tires)
        return rorschach
    
    # creates and returns a thovex Car
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_arr) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tire_wear_arr)
        thovex = Car(engine, battery, tires)
        return thovex
    

    

    
