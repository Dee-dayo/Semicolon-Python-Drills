import unittest

from diary.diary import Diary
from diary.invalid_id_no_error import InvalidIdNoError


class MyTestCase(unittest.TestCase):

    def test_diary_is_created_diary_is_locked(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())

    def test_diary_is_locked_diary_can_be_unlocked_with_password(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())

        diary.unlock_diary('correct_password')
        self.assertFalse(diary.is_locked())

    def test_diary_is_locked_diary_cant_be_unlocked_with_incorrect_password(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())

        diary.unlock_diary('incorrect_password')
        self.assertTrue(diary.is_locked())

    def test_diary_is_unlocked_can_be_locked(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('correct_password')
        self.assertFalse(diary.is_locked())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def test_diary_can_create_entry(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('correct_password')
        self.assertFalse(diary.is_locked())

        diary.create_entry('1st day in semicolon', 'I met Mr. Sikiru')
        self.assertEqual(1, diary.no_of_entries())

    def test_entry_cant_create_if_diary_is_locked(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())

        diary.create_entry('1st day in semicolon', 'I met Mr. Sikiru')
        self.assertEqual(0, diary.no_of_entries())

    def test_entry_is_created_can_find_entry_by_id_no(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('correct_password')
        self.assertFalse(diary.is_locked())

        diary.create_entry('1st day in semicolon', 'I met Mr. Sikiru')
        self.assertEqual(1, diary.no_of_entries())

        entry = diary.find_entry_by_id(1)
        self.assertEqual(entry.title, '1st day in semicolon')
        self.assertEqual(entry.body, 'I met Mr. Sikiru')

    def test_entry_is_created_cant_find_entry_with_incorrect_id(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('correct_password')
        self.assertFalse(diary.is_locked())

        diary.create_entry('1st day in semicolon', 'I met Mr. Sikiru')
        self.assertEqual(1, diary.no_of_entries())

        with self.assertRaises(InvalidIdNoError):
            diary.find_entry_by_id(2)

    def test_entry_is_created_can_delete_entry(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('correct_password')
        self.assertFalse(diary.is_locked())

        diary.create_entry('1st day in semicolon', 'I met Mr. Sikiru')
        self.assertEqual(1, diary.no_of_entries())

        diary.delete_entry(1)
        self.assertEqual(0, diary.no_of_entries())

    def test_entry_is_created_can_update_entry(self):
        diary = Diary('Username', 'correct_password')
        self.assertTrue(diary.is_locked())
        diary.unlock_diary('correct_password')
        self.assertFalse(diary.is_locked())

        diary.create_entry('1st day in semicolon', 'I met Mr. Sikiru')
        entry = diary.find_entry_by_id(1)

        self.assertEqual(entry.title, '1st day in semicolon')
        self.assertEqual(entry.body, 'I met Mr. Sikiru')

        diary.update_entry(1, 'Onboarding semicolon', 'I joined 40 cohort mates')

        self.assertEqual(entry.title, 'Onboarding semicolon')
        self.assertEqual(entry.body, 'I joined 40 cohort mates')