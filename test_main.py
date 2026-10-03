"""Unit tests for the Even and Odd Number Checker."""

import unittest
from main import is_even, check_number


class TestEvenOddChecker(unittest.TestCase):
    """Test suite for is_even and check_number functions."""

    def test_positive_even_numbers(self):
        """Test with various positive even numbers."""
        test_cases = [2, 4, 10, 42, 100, 2468]
        for n in test_cases:
            with self.subTest(n=n):
                self.assertTrue(is_even(n))
                self.assertEqual(check_number(n), "Even")

    def test_positive_odd_numbers(self):
        """Test with various positive odd numbers."""
        test_cases = [1, 3, 7, 19, 99, 1357]
        for n in test_cases:
            with self.subTest(n=n):
                self.assertFalse(is_even(n))
                self.assertEqual(check_number(n), "Odd")

    def test_negative_even_numbers(self):
        """Test with various negative even numbers."""
        test_cases = [-2, -4, -10, -42, -100]
        for n in test_cases:
            with self.subTest(n=n):
                self.assertTrue(is_even(n))
                self.assertEqual(check_number(n), "Even")

    def test_negative_odd_numbers(self):
        """Test with various negative odd numbers."""
        test_cases = [-1, -3, -7, -21, -99]
        for n in test_cases:
            with self.subTest(n=n):
                self.assertFalse(is_even(n))
                self.assertEqual(check_number(n), "Odd")

    def test_zero(self):
        """Test that zero is correctly classified as Even."""
        self.assertTrue(is_even(0))
        self.assertEqual(check_number(0), "Even")

    def test_large_numbers(self):
        """Test with arbitrarily large even and odd numbers."""
        large_even = 10**18  # 1,000,000,000,000,000,000
        large_odd = (10**18) + 1
        large_negative_even = -(10**18)
        large_negative_odd = -((10**18) + 1)

        self.assertTrue(is_even(large_even))
        self.assertEqual(check_number(large_even), "Even")

        self.assertFalse(is_even(large_odd))
        self.assertEqual(check_number(large_odd), "Odd")

        self.assertTrue(is_even(large_negative_even))
        self.assertEqual(check_number(large_negative_even), "Even")

        self.assertFalse(is_even(large_negative_odd))
        self.assertEqual(check_number(large_negative_odd), "Odd")


if __name__ == "__main__":
    unittest.main()
