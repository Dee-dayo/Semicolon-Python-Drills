import unittest

from drills.Drill import Drill


class MyTestCase(unittest.TestCase):
    def test_function_works(self):
        drill = Drill()
        word = "I am a boy"
        drill.get_string(word)
        self.assertEqual(drill.print_string(), 'I am dayo')