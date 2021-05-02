def findNextSquare(sq):
    num_list = []
    for num in range(1,sq):
        num_list.append(num)
    result = sq**.5
    if result in num_list:
        i = num_list.index(result)
        print(num_list)
        print(i)
        next_index = num_list[i]
        next_square = num_list[next_index]**2
        return f"the next square is {next_square}"

    else:
        return -1
findNextSquare(25)








