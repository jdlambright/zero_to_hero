def sum_two_smallest_numbers(numbers):
    '''
    returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
    No floats or non-positive integers will be passed.
    '''
    num_list = numbers
    num_list.sort()

    return num_list[0] + num_list[1]


sum_two_smallest_numbers([7,2,6,3,4,1,9,5])