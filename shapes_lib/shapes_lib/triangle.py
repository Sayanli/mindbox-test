from math import isclose
from shapes_lib.shape import Shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle()

    def _validate_triangle(self):
        if (self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a):
            raise ValueError("Sides do not form a triangle")

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def is_right_angle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return isclose(sides[2]**2, sides[0]**2 + sides[1]**2, rel_tol=1e-9)
