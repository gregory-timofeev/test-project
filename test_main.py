import unittest
from main import get_random_value


class TestSource(unittest.TestCase):

    def test_value_in_range(self):
        """
        Tests if the generated value is within the expected range.
        This test should always pass.
        """
        for _ in range(100):
            with self.subTest():
                result = get_random_value()
                self.assertTrue(1_000 <= result <= 9_999, f"Value {result} out of range [1000, 9999]")
