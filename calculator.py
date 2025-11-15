# https://github.com/ratsareweird/lab11-AM-AA.git
# Partner 1: Austin Aanestad
# Partner 2: Alec McEwen

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    if b == 0: raise ZeroDivisionError
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or a ==1:
        raise ValueError
    return math.log(b,a)# use math library/raise ValueError

def exponent(a, b):
    return a**b