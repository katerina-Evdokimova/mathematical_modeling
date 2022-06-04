from math import sqrt, nan

import numpy as np

from core import Polynomial
from trinomial import QuadraticTrinomial
from scipy.optimize import root

"""

"""


# NEED TO FIX
# A code with a stable error is required
# ------------------------------------------------------------------------------------------------------------
# This method allows you to determine whether there is a necessary root in the found list
# The input receives:
#               divisors - a list with prime numbers;
#               polynomial - the original polynomial in which
#                            it will be necessary to check the numbers from the specified list.
#                            (the data type is a Polynomial.)
# The output is: one root of a given polynomial is obtained.
#         If the root is not found, None is returned.
def _decision(divisors, polynomial: Polynomial):
    result = np.round(root(polynomial, np.array([0.])).x, 8)[0]
    if abs(result) in divisors:
        return result
    return None


# The method allows you to find the prime divisors of a number
# The input is: one integer
# The output is: a list with prime divisors of the input number.
def _divisors(n):
    result = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(float(i))
            result.add(float(n // i))
    return list(result)


# The method allows you to find the roots of a polynomial based on the Buzout method.
# (The description is given in readme.md )
# The input is: polynomial the data type is a Polynomial.
# The output is: a root (a floating-point number);
#                a polynomial with a reduced degree obtained by dividing by x - root (the data type is a polynomial).
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


# This method implements the solution of the polynomial using the Buzu method.
# The input is: polynomial the data type is a Polynomial.
# The output is: a list of roots
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
a = QuadraticTrinomial(1, 4, 5)

print(a.complex_roots)
