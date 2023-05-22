import unittest

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine 

class TestEngine(unittest.TestCase):
    #capulet engine tests. Needs service every 30,000 miles
    def test_capulet_needs_service(self):
        # CapuletEngine(current_milage, last_service_milage)
        engine = CapuletEngine(50000, 15000)
        self.assertTrue(engine.needs_service)

    def test_capulet_does_not_need_service(self):
        # CapuletEngine(current_milage, last_service_milage)
        engine = CapuletEngine(50000, 35000)
        self.assertFalse(engine.needs_service)


    #Willoughby engine tests. Needs service every 60,000 miles
    def test_willoughby_needs_service(self):
        # WilloughbyEngine(current_milage, last_service_milage)
        engine = WilloughbyEngine(65000, 0)
        self.assertTrue(engine.needs_service)

    def test_willoughby_does_not_need_service(self):
        # CapuletEngine(current_milage, last_service_milage)
        engine = CapuletEngine(120000, 100000)
        self.assertFalse(engine.needs_service)


    #Sternman engine tests. Needs service if the warning indicator is on
    def test_sternman_needs_service(self):
        # SternmanEngine(warning light is on)
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service)

    def test_sternman_does_not_need_service(self):
        # SternmanEngine(warning light is on)
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service)