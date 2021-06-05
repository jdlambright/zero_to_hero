'''
#Description:
Write a function that receives a list of 1's and 0's and returns the equivalent in decimal numbers
>max len of the list = 10

 example:
>>> [1,0,1,0,0]
20

Explanation:
Basically depending on where the 1 (True) is it's value, like whit decimals
where
1 1 1 1 1 1 1 1 (binary) =
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 (decimal)

'''

def binary(list):
    bin_list = [1,2,4,8,16,32,64,128,256,512]
    slice_bin_list = bin_list[:len(list)]
    new_bin_list= slice_bin_list[::-1]
    new_list= []

    if len(list) > 10:
        print("sorry the list is too large")

    else:
        for i in range(0,len(list)):
                new_list.append(list[i] * new_bin_list[i])


        print(sum(new_list))






binary([1,0,1,0,0,1,1,1,1,1])