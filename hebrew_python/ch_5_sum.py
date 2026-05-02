# Ask user for a number
# Add this number to sum
# Repeat 2 steps until inserts nothing
# print sum
nums = []
while True:
    print("please insert a number")
    x = input()
    if x == '':
        break
    try:
        nums.append(float(x))
    except ValueError:
        print("please enter a number and not something else")

print(f"your user_sum is : {sum(nums)}")
print(f"from the numbers : {nums}")
    