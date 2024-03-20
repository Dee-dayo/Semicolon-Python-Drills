def highest_repeated_number(numbers):
    number_of_occurence = 0
    answer = 0
    for number in numbers:
        if numbers.count(number) > number_of_occurence:
            number_of_occurence = numbers.count(number)
            answer = number
    return number_of_occurence, answer


def highest_repeated_number2(numbers):
    return max([(numbers.count(number), number) for number in set(numbers)])



print(highest_repeated_number2([1, 2, 2, 3, 4, 2]))

print(highest_repeated_number2([2,3,3,5,6,7]))