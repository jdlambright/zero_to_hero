def findNextSquare(sq):
    result = sq**.5
    if result % 2 == 0 or result % 2 == 1:
        next_square = (result + 1)**2
        return f"the next square is {next_square}"

    else:
        return -1
findNextSquare(37)








