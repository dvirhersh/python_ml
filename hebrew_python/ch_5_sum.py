# Ask user for a number
# Add this number to sum
# Repeat 2 steps until inserts nothing
# print sum
user_sum = 0

print("please enter a number")
try:
    user_input = int(input())
except ValueError:
    print("please enter a number")
while user_input != '':
    user_sum += user_input
    print("please enter another number")
    try:
        user_input = int(input())
    except ValueError:
        print("I see you're done")
        break

print(f"your user_sum is : {user_sum}")
    