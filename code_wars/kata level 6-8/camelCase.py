
def to_camel_case(text):
    original = text
    mylist1 = original.split('_')
    dash= "-"
    next_list = [word + dash for word in mylist1]
    next_string= next_list[0] + ''.join(letter.title() for letter in next_list[1:])
    mylist2 = next_string.split('-')
    camel = mylist2[0] + ''.join(letter.title() for letter in mylist2[1:])

    print(mylist1)
    print(next_list)
    print(next_string)
    print(mylist2)
    print(str(camel))
    return str(camel)

to_camel_case('the-pippi_Is_kawaii')