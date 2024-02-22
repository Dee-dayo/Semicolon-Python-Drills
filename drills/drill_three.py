def return_dictionary(sentence):
    my_dic = {}

    for word in sentence:
        my_dic.update({word: sentence.count(word)})
    return my_dic


result = return_dictionary('the palace is few miles away from the village, but going to the palace to see startups is cool and fun')
print(result)