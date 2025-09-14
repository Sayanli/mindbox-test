import unittest
from shapes_lib.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_area(self):
        tri = Triangle(3, 4, 5)
        self.assertAlmostEqual(tri.area(), 6.0, places=5)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_is_right_angle(self):
        tri = Triangle(3, 4, 5)
        self.assertTrue(tri.is_right_angle())

        tri2 = Triangle(3, 4, 4)
        self.assertFalse(tri2.is_right_angle())
