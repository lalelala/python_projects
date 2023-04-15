import random
print("Welcome to number guessing game!")
number = random.randint(1, 10)
guess = -1
while number != guess:
    guess = int(input("guess a number from 1 to 10."))
    if guess < 10:
        print("invalid")
    if number > guess:
        print("higher")
    elif number < guess:
        print("lower")
    else:
        print("winner!!")
