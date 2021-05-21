def sort_array(source_array):
    num_list = source_array
    sorted_list = []

    for num in num_list:
        if num % 2 == 1:
            sorted_list.append(num)
            sorted_list.sort()
    for num in num_list:
        if num % 2 == 0:
            if num not in sorted_list:
                even_index = num_list.index(num)
                sorted_list.insert(even_index, num)
            else:
                new_start = even_index + 1
                new_even_index = num_list.index(num, new_start)
                sorted_list.insert(new_even_index, num)

    print(sorted_list)
    return sorted_list

sort_array([9, 8, 7, 6, 5, 4, 3,8, 2, 1, 0])






