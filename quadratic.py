import math
def roots(a, b, c):
    discriminante = float(b**2 - 4 * a * c)
    if discriminante < 0:
        return "( )"
    elif discriminante == 0:
        raiz = (math.sqrt(discriminante))
        raiz_1 = float((-b + raiz) / (2 * a))
        return raiz_1
    else:
        raiz = (math.sqrt(discriminante))
        raiz_2 = float((-b - raiz) / (2 * a))
        raiz_1 = float((-b + raiz) / (2 * a))
        return (raiz_1, raiz_2)

print(roots(4, 35, 4))


def value_y(a, b, c, x):
    y = a*x**2 + b*x + c
    return y

print(value_y(1, -3, 2, -1))

def to_string(a, b, c):
    print(f"f(x) = {a} * X^2 + {b} * X + {c}")

to_string(2, -3, 1)

def derivation(a, b, c):
    f"f(x) = {a} * X^2 + {b} * X + {c}"
    d = 2*a
    print(f"f'(x) = {d}x + {b}")

derivation(2, -3, 1)
