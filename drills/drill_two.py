numbers = []

for number in range(16):
    numbers.append(number)


def list_of_numbers():
    return numbers


def add_third_elements(numbers):
    return sum(numbers[2:-1:3])


def sum_of_first_middle_last(numbers):
    return numbers[0] + numbers[len(numbers) // 2] + numbers[-1]


def store_numbers(numbers):
    return set(numbers)


def sum_collection(set_of_numbers):
    return sum(set_of_numbers)


def remove_item(set_of_numbers, number):
    if number in set_of_numbers:
        set_of_numbers.remove(number)
        return number
    else:
        return None


def find_intersection(first_set, second_set):
    return first_set.intersection(second_set)


