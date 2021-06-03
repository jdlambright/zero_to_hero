'''
# Task
Write a function that accepts a string  and returns a dictionary which holds the count of every character in the string.

# Goal
The goal is to learn about the
collections.Counter object!

# Examples:
>>> count("aabbbcdd")
{"a": 2, "b": 3, "c": 1, "d": 2}
>>> count(<object other than str>)
ERROR: expected str, got <object>
'''

def count(string):
    char_dict = {}
    count = 1
    string_list = [char for char in string]

    for char in string_list:

        if char not in char_dict:
            char_dict[char]= count
        elif char in char_dict:
            char_dict[char] +=1

    print(char_dict)

count("abcccddeeffff")