import random

num = random.randint(1,100)
guesses = [0]
correct_guess = False
print("Pick a number between 1 and 100")
print(num)

def warmer_colder():
    global num, guesses, guess
    if abs(num - guesses[-2]) == abs(num - guess):
        print("you are just as close as you were before")
    elif abs(num - guesses[-2]) < abs(num - guess):
        print("You are getting colder")
    elif abs(num - guesses[-2]) > abs(num - guess):
        print("You are getting warmer")

while not correct_guess:
    guess = int(input("what is your guess: "))
    if guess == num:
        print("Great job! You win")
        break
    elif guess > 100:
        print("uh oh! not a valid guess")
    elif abs(num - guess) > 10:
        guesses.append(guess)
        print("Cold")
        warmer_colder()
    elif abs(num - guess) < 10:
        guesses.append(guess)
        print("Hot")
        warmer_colder()