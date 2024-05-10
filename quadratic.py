import math
def roots(a, b, c):
    x = b**2 - 4 * a * c
    if x < 0:
        return"( )"
    else:
        sr1 = -b + math.sqrt(x)
        sr2 = -b - math.sqrt(x)
        r1 = sr1 /(2 * a) 
        r2 = sr2 /(2 * a)
        if r1 == r2:
            return f"({r1})"
        elif r1 != r2:
            return f"({r1}, {r2})"
        else:
            return "( )"

def value_y(a, b, c, x):
    y = a * x**2 + b * x + c
    return y


def to_string(a, b, c):
    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    elif a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"


def derivation(a, b, c):
    a= a ** 2
    if a != 0 and b != 0:
        return f"f'(x) = {a} * X + {b}"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    elif a != 0 and b == 0:
        return f"f'(x) = {a} * X"
    else: 
        return "f'(x) = 0"
