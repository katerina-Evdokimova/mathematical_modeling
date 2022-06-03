from math import sqrt

import numpy as np

from core import Polynomial
from trinomial import QuadraticTrinomial
from scipy.optimize import root


def _decision(divisors, polynomial: Polynomial):
    result = root(polynomial, np.array([0.]))
    if abs(np.round(result.x, 8)[0]) in divisors:
        return np.round(result.x, 8)[0]
    return None


def _divisors(n):
    result = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(float(i))
            result.add(float(n // i))
    return list(result)


def root_polynomial(polynomial: Polynomial):
    if sum(polynomial) == 0:
        return 1, polynomial // Polynomial(1, -1)
    elif sum([i for i in polynomial if i % 2 == 0]) == sum([i for i in polynomial if i % 2 != 0]):
        return -1, polynomial // Polynomial(1, 1)
    else:
        divisors = _divisors(abs(polynomial[0]))
        root = _decision(divisors, polynomial)
        if root:
            return root, polynomial // Polynomial(1, -root)
        else:
            return None, None


def bezout(polynomial: Polynomial):
    roots = []
    if len(polynomial) != 4:
        return 'error length polynomial < 4'
    if polynomial[4] != 1:
        polynomial /= polynomial[4]
    # if polynomial[4] == 0:
    #     return ZeroDivisionError("Can't divide a Polynomial by 0")
        # print(polynomial)
    root, polynomial2 = root_polynomial(polynomial)
    roots.append(root)
    if polynomial2:
        root, polynomial3 = root_polynomial(polynomial2)
        roots.append(root)
        if polynomial3:
            polynomial4 = QuadraticTrinomial(polynomial3[2], polynomial3[1], polynomial3[0])
            x = polynomial4.complex_roots
            roots.append(x[0])
            roots.append(x[1])
    return roots


print(bezout(Polynomial(1, 3, 7, -21, -26)))  # [-1, 2, (-2+3j), (-2-3j)]
