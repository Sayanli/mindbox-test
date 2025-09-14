import unittest
from shapes_lib.circle import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), 3.1415926535, places=5)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
