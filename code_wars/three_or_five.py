def solution(number):
    mylist = []

    for n in range(0,number):
        if n % 3 == 0 or n % 5 == 0:
            mylist.append(n)
    print(mylist)
    print(sum(mylist))
    return sum(mylist)

solution(25)