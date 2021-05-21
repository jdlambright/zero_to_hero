'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a
single integer N. Write a method that takes the array as an argument and returns this "outlier" N
'''

def find_outlier(integers):
    for num in integers:
        if integers[0] % 2 == 0 and integers[1] % 2 == 0:
            if num % 2 == 1:
                print(num)
                return num
        elif integers[0] % 2 == 1 and integers[1] % 2 == 1:
            if num % 2 == 0:
                print(num)
                return num
        else:
            if integers[2] % 2 == 0:
                if num % 2 == 1:
                    print(num)
                    return num
            else:
                if num % 2 == 0:
                    print(num)
                    return num





find_outlier([28, 3, 1719, 19,  11, 13, -21])


'''
other solutions I liked

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def find_outlier(integers):
    odd = filter(lambda x: x % 2 == 1, integers)
    even = filter(lambda x: x % 2 == 0, integers)
    return odd[0] if len(odd) == 1 else even[0]



'''