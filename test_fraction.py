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

    def test_as_mixed_number(self):
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 1/3")

    def test_is_zero(self):
        f = Fraction(0, 5)
        self.assertTrue(f.is_zero())

    def test_is_integer(self):
        f = Fraction(10, 2)
        self.assertTrue(f.is_integer())

    def test_is_proper(self):
        f = Fraction(1, 3)
        self.assertTrue(f.is_proper())

    def test_is_unit(self):
        f = Fraction(1, 1)
        self.assertTrue(f.is_unit())

    def test_is_adjacent_to(self):
        # Case 1: Adjacent fractions
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertTrue(f1.is_adjacent_to(f2))  # True, as |2*4 - 3*3| = 1

        # Case 2: Non-adjacent fractions
        f3 = Fraction(5, 6)
        self.assertFalse(f1.is_adjacent_to(f3))  # False, as |2*6 - 5*3| ≠ 1

        # Case 3: Fraction and integer adjacent
        f4 = Fraction(2, 1)
        self.assertTrue(f4.is_adjacent_to(3))  # True, as |2*1 - 3*1| = 1

        # Case 4: Fraction and integer non-adjacent
        self.assertFalse(f4.is_adjacent_to(4))  # False, as |2*1 - 4*1| ≠ 1

        # Case 5: Invalid type for 'other'
        with self.assertRaises(TypeError):
            f1.is_adjacent_to("string")

    def test_comparisons(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertTrue(f1 < f2)
        self.assertTrue(f2 > f1)
        self.assertTrue(f1 <= Fraction(1, 2))
        self.assertTrue(f2 >= Fraction(2, 3))

    # Test for gcd method
    def test_gcd_valid(self):
        f = Fraction(24, 36)
        self.assertEqual(f.gcd(24, 36), 12)  # GCD of 24 and 36 is 12

    def test_gcd_invalid(self):
        with self.assertRaises(TypeError):
            Fraction(24, 36).gcd(24, "string")  # gcd with invalid type

    def test_string_representation(self):
        f1 = Fraction(5, 2)
        self.assertEqual(str(f1), "5/2")  # Non-integer denominator

        f2 = Fraction(3, 1)
        self.assertEqual(str(f2), "3")  # Integer denominator

    def test_mixed_number_representation(self):
        f1 = Fraction(7, 3)
        self.assertEqual(f1.as_mixed_number(), "2 1/3")  # Mixed number

        f2 = Fraction(5, 2)
        self.assertEqual(f2.as_mixed_number(), "2 1/2")  # Mixed number

    def test_edge_case_integer_zero(self):
        f = Fraction(0, 1)
        self.assertTrue(f.is_zero())  # Zero fraction

    def test_edge_case_negative_fraction(self):
        f = Fraction(-2, 3)
        self.assertEqual(str(f), "-2/3")  # Negative fraction

    def test_edge_case_negative_integer(self):
        f = Fraction(-2, 1)
        self.assertEqual(str(f), "-2")  # Negative integer as fraction

if __name__ == '__main__':
    unittest.main()
