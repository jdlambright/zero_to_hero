'''
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...
'''



num_dict ={"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight":8, "nine": 9}
op_dict ={"plus": "+", "minus": "-", "times": "*", "divided_by": "/"}

a = num_dict["zero"].values(), op_dict["plus"].values(), num_dict["two"].values()

print(a)
