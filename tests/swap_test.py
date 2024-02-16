import unittest

from drills import swapping


class MyTestCase(unittest.TestCase):
    def test_can_swap_first_two_string(self):
        self.assertEqual('xyc abz', swapping.swap_first_two_strings('abc', 'xyz'))
        self.assertEqual('lmcde abnop', swapping.second_attempt('abcde', 'lmnop'))
        self.assertEqual('lmcde abnop', swapping.swap_first_two_strings('abcde', 'lmnop'))