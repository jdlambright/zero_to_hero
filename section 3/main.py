
def duplicate_count(text):
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

# def count_char(text):
#   count = {}
#   for ch in text:
#     # don't count frequency of spaces
#     if ch == ' ' or ch == '\t':
#       continue
#     # If char already in dictionary increment count
#     # otherwise add char as key and 1 as value
#     if ch in count:
#       count[ch] += 1
#     else:
#       count[ch] = 1
#     for k, v in count.items():
#       print('Charcater {} occurs {} times'.format(k,v))
