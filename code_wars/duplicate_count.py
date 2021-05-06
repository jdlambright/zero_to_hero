
def duplicate_count(text):
    '''
    this function looks at a string and determines if there are more than one of the same character regardless of case
    :param text:
    :return: the number of characters that have duplicates
    '''
    count_dict = {}

    for char in text:
        string = text
        count =string.lower().count(char)

        if count > 1:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        else:
            continue
    print(len(count_dict))
    print(count_dict)




duplicate_count("aAbbc ")