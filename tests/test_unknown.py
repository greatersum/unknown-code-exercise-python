import unittest

from unknown.get_number import get_number


class Tests(unittest.TestCase):
    def test_zero_returns_zero(self):
        self.assertEqual(get_number(0), 0)
