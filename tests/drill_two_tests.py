import unittest
from drills import drill_two


class MyTestCase(unittest.TestCase):
    def test_list_of_numbers_from_one_to_ten(self):
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(expected, drill_two.list_of_numbers())

    def test_add_third_elements_within_a_list(self):
        actual = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(18, drill_two.add_third_elements(actual))

    def test_function_calculate_sum_of_first_middle_last_elements(self):
        self.assertEqual(6, drill_two.sum_of_first_middle_last([1, 2, 3]))

        actual = [1, 2, 3, 4, 5]
        self.assertEqual(9, drill_two.sum_of_first_middle_last(actual))

    def test_function_collects_ten_numbers_but_no_duplicate_elements(self):
        actual = {1,2,3,4,5,3,4,2,6,7,8,9,10}
        self.assertEqual({1,2,3,4,5,6,7,8,9,10}, drill_two.store_numbers(actual))

    def test_function_sums_set_of_numbers(self):
        set_of_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.assertEqual(55, drill_two.sum_collection(set_of_numbers))

    def test_function_takes_set_remove_element(self):
        set_of_numbers = {1, 2, 3, 4, 5}
        self.assertEqual(5, drill_two.remove_item(set_of_numbers, 5))
        self.assertEqual(None, drill_two.remove_item(set_of_numbers, 6))

    def test_function_returns_interset_between_two_sets(self):
        set_of_numbers = {1, 2, 3, 4, 5}
        set_of_numbers_two = {1, 6, 7, 8, 2, 4}
        self.assertEqual({1,2,4}, drill_two.find_intersection(set_of_numbers, set_of_numbers_two))
