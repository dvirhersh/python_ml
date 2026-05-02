# get a number n
# calc n!
    # multiply all integers numbers between n..1

# def factorial(n: int) -> int:
#     sum = 1
#     for i in range(1, n + 1):
#         sum *= i
#     return sum

def factorial(n):
    # if n == 1:
    if n == 0:
        return 1
    return factorial(n-1)*n

print(factorial(3))
print(factorial(4))
print(factorial(0))
print(factorial(100))
# print(factorial(1000))