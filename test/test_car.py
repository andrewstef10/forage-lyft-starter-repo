import unittest
from datetime import datetime
from CarFactory import CarFactory

#           Service Info:
# Capulet Engine	Once every 30,000 miles
# Willoughby Engine	Once every 60,000 miles
# Sternman Engine	Only when the warning indicator is on
#
# Spindler Battery	Once every 2 years
# Nubbin Battery	Once every 4 years

class TestCapulet(unittest.TestCase):
    # Capulet contains capulet engine and spindler battery

    def test_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_calliope(current_date, last_service_date, 40000, 0)
        self.assertTrue(car.needs_service)

    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        car = CarFactory.create_calliope(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)

    def test_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_calliope(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)


class TestGlissade(unittest.TestCase):
    # Glissade contains Willoughby engine and spindler battery

    def test_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_gilssade(current_date, last_service_date, 70000, 0)
        self.assertTrue(car.needs_service)

    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        car = CarFactory.create_gilssade(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)

    def test_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_gilssade(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)

class TestPalindrome(unittest.TestCase):
    # Palindrome contains Sternman engine and spindler battery

    def test_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_palindrome(current_date, last_service_date, True)
        self.assertTrue(car.needs_service)

    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        car = CarFactory.create_calliope(current_date, last_service_date, False)
        self.assertTrue(car.needs_service)

    def test_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_calliope(current_date, last_service_date, False)
        self.assertTrue(car.needs_service)


class TestRorschach(unittest.TestCase):
    #Rorschach contains Willouby Engine and Nubbin battery

    def test_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_rorschach(current_date, last_service_date, 70000, 0)
        self.assertTrue(car.needs_service)

    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        car = CarFactory.create_rorschach(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)

    def test_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_rorschach(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)


class TestThovex(unittest.TestCase):
    #Thovex contains Capulet Engine and Nubbin battery

    def test_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_calliope(current_date, last_service_date, 40000, 0)
        self.assertTrue(car.needs_service)

    def test_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        car = CarFactory.create_calliope(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)

    def test_does_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        car = CarFactory.create_calliope(current_date, last_service_date, 20000, 0)
        self.assertTrue(car.needs_service)