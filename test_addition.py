import unittest
from addition import add

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 5), 4)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

if __name__ == "__main__":
    unittest.main()
