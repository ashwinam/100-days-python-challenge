# calculate factorial

'''
factorial(5):
5 * 4 * 3 * 2 * 1 
120
'''

# factorial using iteration

def factorial_using_loops(num):
    fact = 1
    for i in range(num, 0, -1):
        fact *= i
    return fact

print(factorial_using_loops(5))

# factorial_using_recursion

def factorial_using_recursion(num):
    if (num == 0 or num == 1):
        return 1
    return num * factorial_using_recursion(num - 1)

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

print(factorial_using_recursion(6))

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(0, 13):
    print(fib(i), end=" ")