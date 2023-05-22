import unittest
from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestBattery(unittest.TestCase):
    # spindler batter tests. Needs service once every 2 years
    def test_spindler_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service)

    def test_spindler_does_not_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service)


    # Nubbin batter tests. Needs service once every 4 years
    def test_nubbin_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service)

    def test_spindler_does_not_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service)
