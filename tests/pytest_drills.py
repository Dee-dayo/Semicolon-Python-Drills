import pytest

from drills import python_drill


def test_get_length_function():
    my_list = [2, 3, 4, 5, 6, 7, 8, 9, 5, 3]
    assert python_drill.get_length(my_list) == 10


def test_function_sum_all_element_at_even_position():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert python_drill.sum_length_of_array_even_position(my_list) == 30


def test_function_sum_all_element_at_odd_position():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert python_drill.sum_length_of_array_odd_position(my_list) == 25