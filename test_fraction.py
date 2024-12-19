import unittest
from TP07 import Fraction

class TestFraction(unittest.TestCase):

    def test_initialization_valid(self):
        f = Fraction(1, 2)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

    def test_initialization_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_subtraction(self):
        f1 = Fraction(5, 6)
        f2 = Fraction(1, 6)
        result = f1 - f2
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 3)

    def test_multiplication(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 5)
        result = f1 * f2
        self.assertEqual(result.numerator, 8)
        self.assertEqual(result.denominator, 15)

    def test_division(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 5)
        result = f1 / f2
        self.assertEqual(result.numerator, 15)
        self.assertEqual(result.denominator, 8)

    def test_equality(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 6)
        self.assertTrue(f1 == f2)

    def test_invalid_addition(self):
        with self.assertRaises(TypeError):
            f1 = Fraction(1, 2)
            f1 + "string"

if __name__ == '__main__':
    unittest.main()
