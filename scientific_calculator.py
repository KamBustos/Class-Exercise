import math

def check_numeric_input(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a numeric value")

def sin(x):
    check_numeric_input(x)
    return math.sin(math.radians(x))

def cos(x):
    check_numeric_input(x)
    return math.cos(math.radians(x))

def tan(x):
    check_numeric_input(x)
    return math.tan(math.radians(x))

def sqrt(x):
    check_numeric_input(x)
    if x < 0:
        raise ValueError("Input must be non-negative")
    return math.sqrt(x)

def log(x):
    check_numeric_input(x)
    if x <= 0:
        raise ValueError("Logarithm is undefined for zero or negative values")
    return math.log(x)

def exp(x):
    check_numeric_input(x)
    return math.exp(x)

def asin(x):
    check_numeric_input(x)
    if not -1 <= x <= 1:
        raise ValueError("Input must be within [-1, 1] range for asin")
    return math.degrees(math.asin(x))

def acos(x):
    check_numeric_input(x)
    if not -1 <= x <= 1:
        raise ValueError("Input must be within [-1, 1] range for acos")
    return math.degrees(math.acos(x))

def atan(x):
    check_numeric_input(x)
    return math.degrees(math.atan(x))

def sinh(x):
    check_numeric_input(x)
    return math.sinh(x)

def cosh(x):
    check_numeric_input(x)
    return math.cosh(x)

def tanh(x):
    check_numeric_input(x)
    return math.tanh(x)