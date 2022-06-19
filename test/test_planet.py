from mrk import Planet
from unittest import TestCase


class TestPlanetCoordinates(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.planet_height = 20
        cls.planet_width = 20
        cls.planet = Planet(cls.planet_width, cls.planet_height)

    def test_wrap_x(self):
        for i in range(0,100):
            current_coordinates = self.planet.get_coordinates(i, 0)
            self.assertLess(current_coordinates[0], 20)

    def test_wrap_y(self):
        for i in range(0,100):
            current_coordinates = self.planet.get_coordinates(0, i)
            self.assertLess(current_coordinates[1], 20)


class TestPlanetPositionKey(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.planet_height = 20
        cls.planet_width = 20
        cls.planet = Planet(cls.planet_width, cls.planet_height)

    def test_position_key(self):
        for i in range(0, 100):
            for j in range(0, 100):
                key = self.planet.position_key(i, j)
                self.assertRegex(key, r"^[0-9]{1,2}:[0-9]{1,2}$")
