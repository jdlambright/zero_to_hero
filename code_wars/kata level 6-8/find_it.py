#you will be given a list of numbers
#find the number that appears an odd number of times

def find_it(seq):
    num_dict = {}
    count = 1

    for num in seq:
        if num not in num_dict:
            num_dict[num]= count
        elif num in num_dict:
            num_dict[num] +=1

    print(num_dict)

    for key, value in num_dict.items():
        if value % 2 == 1:
            print(key)
            return key





find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])