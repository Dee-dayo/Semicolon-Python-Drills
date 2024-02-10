sample_list = list(range(1, 11))

def get_length(sample_list):
    length = 0
    for number in sample_list:
        length += 1
    return length


def sum_length_of_array_even_position(list_of_numbers):
    return sum(list_of_numbers[1::2])


def sum_length_of_array_odd_position(list_of_numbers):
    sum = 0
    for number in range(0, len(list_of_numbers), 2):
        sum += list_of_numbers[number]

    return sum


def largest_element(list_of_numbers):
    highest = list_of_numbers[0]

    for number in list_of_numbers:
        if number > highest:
            highest = number

    return highest


def multiply_third_positions(list_of_numbers):
    multiply = 1
    for number in range(2, len(list_of_numbers), 3):
        multiply *= list_of_numbers[number]

    return multiply


def smallest_element(list_of_numbers):
    smallest = list_of_numbers[0]

    for number in list_of_numbers:
        if number < smallest:
            smallest = number

    return smallest


def average_of_element(list_of_numbers):
    average = sum(list_of_numbers) / len(list_of_numbers)
    return average


