import unittest
import math
import rectangle
import circle
import square


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_square_area2(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 50)

    def test_negative_area(self):
        res = rectangle.area(-4, 2)
        self.assertEqual(res, 8)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)
       
    def test_square_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_negative_perimeter(self):
        res = rectangle.perimeter(-4, 2)
        self.assertEqual(res, 12)

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
       
    def test_normal_area(self):
        res = circle.area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_negative_area(self):
        res = circle.area(-10)
        self.assertEqual(res, 100 * math.pi)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
       
    def test_normal_perimeter(self):
        res = circle.perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def test_negative_perimeter(self):
        res = circle.perimeter(-10)
        self.assertEqual(res, 20 * math.pi)


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
       
    def test_normal_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_negative_area(self):
        res = square.area(-10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
       
    def test_normal_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_negative_perimeter(self):
        res = square.perimeter(-10)
        self.assertEqual(res, 40)