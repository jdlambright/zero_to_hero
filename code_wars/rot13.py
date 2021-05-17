'''
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation"
'''

def rot13(message):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
               "u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m",
               "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
               "U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"]
    new_message = []
    for letter in message:
        if letter in letters:
            idx = letters.index(letter)
            new_message.append(letters[idx + 13])
        else:
            new_message.append(letter)
    new_message= " ".join(new_message)
    print(new_message)
    return new_message





rot13("This is a test")