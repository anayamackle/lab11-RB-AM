#https://github.com/anayamackle/lab11-RB-AM
#Partner 1: Anaya Mackle
#Partner 2: Ryan Buehler
import math
def add(a, b): 
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return b / a
def log(a,b):
    if a <= 0:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b,a)
def exp(a,b):
    return a ** b


