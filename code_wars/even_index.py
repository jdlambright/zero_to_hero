def find_even_index(arr):

    for i in arr:
        left_slice = arr[:i]
        right_slice = arr[i + 1:]
        left_total = sum(left_slice)
        right_total = sum(right_slice)

        if left_total == right_total:
            print(left_slice)
            print(right_slice)
            print(arr.index(i)+1)
            return arr.index(i)+1
        else:
            print(left_slice)
            print(right_slice)
            print(-1)
            return -1





find_even_index([1,2,3,4,3,2,1])