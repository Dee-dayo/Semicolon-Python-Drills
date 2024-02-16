def swap_first_two_strings(first_string, second_string):
    temp = ''
    temp2 = ''

    for i in second_string[:2]:
        temp = temp + i

    temp = temp + first_string[2:]

    for i in first_string[:2]:
        temp2 = temp2 + i
    temp2 = temp2 + second_string[2:]

    output = temp + ' ' + temp2
    return output

def second_attempt(first_string, second_string):
    return second_string[:2] + first_string[2:] + ' ' + first_string[:2] + second_string[2:]









def meshack_swap(i, j):
    answer1 = i[0] + i[1] + j[2]
    answer2 = j[0] + j[1] + i[2]
    return answer1 + ' ' + answer2


def meshack_swap2(i, j):
    answer1 = ''
    answer2 = ''
    for num in i[0:2]:
        answer1 += num
    answer1 += j[2]

    for num in j[0:2]:
        answer2 += num
    answer2 += i[2]

    return answer1 + ' ' + answer2


num1 = 'abc'
num2 = 'xyz'
print(meshack_swap2(num1, num2))
