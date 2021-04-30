def summer69(arr):

    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total



summer69([1,3,5])

