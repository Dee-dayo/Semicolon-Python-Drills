# class Drill(object):
#     def __init__(self):
#         self.final = []
#
#     def value(self, *args):
#         for arg in args:
#             ans = (2 * 50 * arg) / 30
#             self.final.append(round(ans ** 0.5))
#
#         return ', '.join(map(str, self.final))
#
# drill = Drill()
# drill.value(100, 150, 180)
# print(drill)


def value(*args):
    final = []
    for arg in args:
        ans = (2 * 50 * arg) / 30
        final.append(round(ans ** 0.5))

    return ', '.join(map(str, final))


# print(value(100, 150, 180))


def count_letter_number(sentence):
    letters = 0
    digits = 0

    for letter in sentence:
        if letter.isalpha():
            letters += 1
        elif letter.isdigit():
            digits += 1

    my_dict = {'LETTERS': letters, 'DIGITS': digits}

    # return f'LETTERS {letters} DIGITS {digits}'
    return my_dict


# print(count_letter_number('hello world! 123'))


def count_letter_case(sentence):
    upper = 0
    lower = 0

    for letter in sentence:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    return f'UPPER CASE {upper} LOWER CASE {lower}'


print(count_letter_case('Hello world!'))

