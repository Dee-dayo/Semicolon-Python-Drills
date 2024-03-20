import unittest

from drills.javascript_drill import highest_repeated_number


class MyTestCase(unittest.TestCase):
    def test_function_works(self):
        self.assertEqual((3, 3), highest_repeated_number([1, 3, 3, 3, 4, 2]))
