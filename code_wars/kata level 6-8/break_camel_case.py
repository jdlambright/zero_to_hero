#Complete the solution so that the function will break up camel casing, using a space between words

def solution(s):
    start_index = 0
    next_index = start_index + 1

    for i in s:
        if i.isupper():
            space_index = s.index(i-1)
            insert()








solution("camelCase")