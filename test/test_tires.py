import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestTires(unittest.TestCase):
    # carrigan tires need service if any of the values is >= 0.9
    def test_carrigan_needs_service(self):
        tires = CarriganTire([0.7, 0.8, 0.8, 0.9])
        self.assertTrue(tires.needs_service)

    def test_carrigan_does_not_need_service(self):
        tires = CarriganTire([0.7, 0.8, 0.8, 0.8])
        self.assertFalse(tires.needs_service)

    
    # Octoprime tires need service if sum of arr values is >= 3
    def test_octoprime_needs_service(self):
        tires = OctoprimeTire([0.7, 0.8, 0.8, 0.7])
        self.assertTrue(tires.needs_service)

    def test_octoprime_does_not_need_service(self):
        tires = OctoprimeTire([0.7, 0.8, 0.8, 0.6])
        self.assertTrue(tires.needs_service)