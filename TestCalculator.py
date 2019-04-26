import unittest
from Calculator import *

class TestCalculator(unittest.TestCase):
    def test_int_add_1(self):
        self.assertEqual(add(9, 3), 12)
    
    def test_float_add(self):
        self.assertEqual(add(4.2, 3), 7.2)

    def test_int_minus(self):
        self.assertEqual(minus(9, 3), 6)

    def test_float_minus(self):
        self.assertEqual(minus(4.2, 3.2), 1.0)
    
    def test_int_multiply(self):
        self.assertEqual(multiply(3, 6), 18)

    def test_float_multiply(self):
        self.assertEqual(multiply(1.2, 3.2), 3.84)

    def test_int_divide(self):
        self.assertEqual(divide(9, 3), 3)

    def test_int_divide_2(self):
        self.assertEqual(divide(9, 0), "infinity")
    
    def test_float_divide(self):
        self.assertEqual(divide(9.3, 1.5), 6.2)

if __name__ == '__main__':
    unittest.main()