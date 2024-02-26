import unittest

from diary.diaries import Diaries


class MyTestCase(unittest.TestCase):
    def test_diary_can_be_added_to_diaries(self):
        diaries = Diaries()
        diaries.add('username', 'correct_password')
        self.assertEqual(1, diaries.no_of_diaries())

    def test_diary_can_be_find_by_username(self):
        diaries = Diaries()
        diaries.add('username', 'correct_password')

        found_diary = diaries.find_by_username('username')
        self.assertEqual('username', found_diary.get_username())

    def test_diaries_can_delete_diary_by_username_password(self):
        diaries = Diaries()
        diaries.add('username', 'correct_password')
        self.assertEqual(1, diaries.no_of_diaries())

        diaries.delete('username', 'correct_password')
        self.assertEqual(0, diaries.no_of_diaries())