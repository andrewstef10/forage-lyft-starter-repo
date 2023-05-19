from abc import ABC

from car_components import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_on: bool):
        super().__init__()
        self.warning_light_is_on = warning_light_on

    # determines if the Sternman engine needs service
    def needs_service(self):
        return self.warning_light_on
