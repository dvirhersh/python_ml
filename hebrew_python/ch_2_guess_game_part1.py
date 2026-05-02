# pick a number to be guessed

# ask user to guess a number
# get the guessed number
# resond with right / wrong
# repeat last 3 steps

number = 13
guessed = 0

while number != guessed:
    print("Please guess a number 1-100")
    guessed = int(input())
    if number == guessed:
        print('Right!')
    else:
        print('Wrong!')