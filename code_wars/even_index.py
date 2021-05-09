def find_even_index(arr):
    i = 0
    equal_slices = False
    while not equal_slices:
        left_slice = arr[:i]
        right_slice = arr[i + 1:]
        left_total = sum(left_slice)
        right_total = sum(right_slice)

        if left_total == right_total:
            print(i)
            equal_slices = True
            return i
        else:
            i+= 1

        if i > len(arr):
            if left_total != right_total:
                break
    print (-1)
    return -1


#find_even_index([1,2,3,4,3,2,1])
find_even_index([20,10,30,10,40,10,15,35])