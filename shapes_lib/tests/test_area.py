import unittest
from shapes_lib.shape import area
from shapes_lib.triangle import Triangle
from shapes_lib.circle import Circle

class TestAreaFunction(unittest.TestCase):
    def test_area_circle(self):
        c = Circle(2)
        self.assertAlmostEqual(area(c), 3.14159 * 4, places=4)

    def test_area_triangle(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(area(t), 6.0, places=5)
