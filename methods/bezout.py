from math import sqrt

import numpy as np

from scipy.optimize import root

from methods.Polynomials import Polynomials, QuadraticTrinomials
from methods.checking_polynomial import checking

"""
Bezu's theorem states that the remainder of the division of the polynomial P(x) by the binomial x - a is equal to P(a).
 For us, it is not the theorem itself that is important, but the consequence of it :

If the number _a_ is the root of the polynomial P(x), then the polynomial 
P(x) = a0*x^n + a1*x^(n - 1) + a2*x^(n - 2) + ... + an is divisible without remainder by the binomial x - a.
"""

'''https://en.wikipedia.org/wiki/Newton%27s_method
To optimize the root finding, the Newton method was chosen'''


# ------------------------------------------------------------------------------------------------------------
# This method allows you to determine whether there is a necessary root in the found list
# The input receives:
#               divisors - a list with prime numbers;
#               polynomial - the original polynomial in which
#                            it will be necessary to check the numbers from the specified list.
#                            (the data type is a Polynomial.)
# The output is: one root of a given polynomial is obtained.
#         If the root is not found, None is returned.
def _decision(divisors, polynomial: Polynomials):
    for i in divisors:
        if i == i - polynomial(i) / polynomial.nth_derivative()(i):
            return i
        if -i == -i - polynomial(-i) / polynomial.nth_derivative()(-i):
            return -i
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
def root_polynomial(polynomial: Polynomials):
    if sum(polynomial) == 0:
        return 1, polynomial // Polynomials(1, -1)
    elif sum([i for i in polynomial if i % 2 == 0]) == sum([i for i in polynomial if i % 2 != 0]):
        return -1, polynomial // Polynomials(1, 1)
    else:
        divisors = _divisors(abs(polynomial[0]))
        root = _decision(divisors, polynomial)
        if root:
            return root, polynomial // Polynomials(1, -root)
        else:
            return None, None


# This method implements the solution of the polynomial using the Buzu method.
# The input is: polynomial the data type is a Polynomial.
# The output is: a list of roots
def bezout(polynomial: Polynomials):
    roots = []
    flag, result = checking(polynomial, 4)
    if not flag:
        return result
    else:
        polynomial = result
    root, polynomial2 = root_polynomial(polynomial)
    roots.append(root)
    if polynomial2:
        root, polynomial3 = root_polynomial(polynomial2)
        roots.append(root)
        if polynomial3:
            polynomial4 = QuadraticTrinomials(polynomial3[2], polynomial3[1], polynomial3[0])
            x = polynomial4.complex_roots
            roots.append(x[0])
            roots.append(x[1])
    return roots
