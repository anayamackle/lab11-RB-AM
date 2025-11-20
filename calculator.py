#https://github.com/anayamackle/lab11-RB-AM
#Partner 1: Anaya Mackle
#Partner 2: Ryan Buehler
import math
def square_root(a):
    if a<0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)
def add(a, b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return b / a
def logarithm(a,b):
    if a <= 0:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b,a)
def exponent(a,b):
    return a ** b


