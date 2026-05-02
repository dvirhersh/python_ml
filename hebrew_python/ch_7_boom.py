# ask user for integer
# Get user input (n)
# print numbers from 1 to n, 
# substitue numbers divisible by 7
# or contain 7 as a digit with 'BOOM!'

# For each number in 1..n, if it's divisible by 7 .. 
# print 'Boom!' 
# else print the number
import time
n = int(input('please insert a number to count up to.\n\n'))

for i in range(1, n+1):
    if i % 7 == 0:
        print("Boom!")
    elif '7' in str(i):
        print("Boom!")
    else:
        print(i)
