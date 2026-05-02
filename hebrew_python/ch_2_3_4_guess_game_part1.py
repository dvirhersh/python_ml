# pick a random number to be guessed

# ask user to guess a number
# get the guessed number
# if input is not a number tell the user and return to ask a number
# respond with right/too high /too low 
# repeat last 3 steps
import random

number = 13
number = random.randint(1, 100)
guessed = 0

while number != guessed:
    print("Please guess a number 1-100")
    try:
        guessed = int(input())
    except ValueError:
        print("Please enter an integer!")
        continue
    if number == guessed:
        print('Right!')
    elif number < guessed:
        print("too high")
    else:
        print("too low")