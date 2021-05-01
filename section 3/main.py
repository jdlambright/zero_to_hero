def up_low(s):
    lower_letters = []
    upper_letters = []

    for letter in s:
        if letter.islower() == True:
            lower_letters.append(letter)
        elif letter.isupper() == True:
            upper_letters.append(letter)

    print(f"there are {len(lower_letters)} lower case letters in this string")
    print(f"there are {len(upper_letters)} upper case letters in this string")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)