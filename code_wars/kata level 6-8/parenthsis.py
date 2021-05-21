def valid_parentheses(string):
    p_list = [item for item in string]
    left_count = 0
    right_count = 0
    start_index = 0

    for item in p_list:
        if "(" in p_list:
            left_count += 1
        if ")" in p_list:
            right_count += 1
        if left_count == right_count:
            print("true")
            return True
    print("false")
    return False




valid_parentheses("()(")