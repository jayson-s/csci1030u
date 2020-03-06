"""
Factorial Loop:
Loop version of Factorial
"""

"""
def factorialLoop (n) :
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorialLoop(5))
"""

"""
Factorial Recursion:
Recursion version of Factorial
"""

"""
def factorialRecursion(n):
    if n == 1:
        return 1
    return factorialRecursion(5)

print(factorialRecursion(5))
"""


def fib(n):
    if n<= 1:
        return n
    return fib(n-1) + fib(n-2)
