import unittest

from drills import python_drill


class MyTestCase(unittest.TestCase):
    def test_get_length_function(self):
        my_list = [2, 3, 4, 5, 6, 7, 8, 9, 5, 3]
        self.assertEqual(10, python_drill.get_length(my_list))  # add assertion here

    def test_function_sum_all_element_at_even_position(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(30, python_drill.sum_length_of_array_even_position(my_list))


    def test_function_sum_all_element_at_odd_position(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(25, python_drill.sum_length_of_array_odd_position(my_list))


    def test_function_multiplies_element_at_third_positions(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(162, python_drill.multiply_third_positions(my_list))



    def test_get_largest_element_in_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(10, python_drill.largest_element(my_list))


    def test_get_smallest_element_in_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(1, python_drill.smallest_element(my_list))


    def test_function_can_get_average_of_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(5.5, python_drill.average_of_element(my_list))