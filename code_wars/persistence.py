'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit.
'''
import numpy
def persistence(n):
    count = 0
    while False:
        if n < 10:
            print(count)
            return count
        else:
            res = [int(x) for x in str(n)]
            product = numpy.prod(res)
            n = product
            count += 1

    print(res)
    print(product)






persistence(39)