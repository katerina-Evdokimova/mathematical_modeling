from cmath import sqrt

import numpy as np

from methods.Polynomials import Polynomials, QuadraticTrinomials
from methods.checking_polynomial import checking


# A modern method for solving equations of the fourth degree, based on the method of Cardano and Descartes.
# (More information about the Cardano method is written in readme.md)
# Input data: A polynomial with integer coefficients of the fourth degree.
# Output: list of roots
def method_cardano_descartes(polynomial: Polynomials):

    flag, result = checking(polynomial, 4)
    if not flag:
        return result

    a1 = polynomial[1]
    a2 = polynomial[2]
    a3 = polynomial[3]

    const = a3 * 0.125
    const1 = a3 * const
    const2 = 3 * const1
    const3 = const * 2

    p = a2 - const2
    r = a1 - a3 * (a2 * 0.5 + const1)
    q = polynomial[0] - const3 * (a1 + const3 * (a2 - const2 * 0.5))

    '''Since the solve() method is designed for integer coefficients, we have difficulties with floating-point 
    coefficients. Therefore, it was temporarily decided to use the method of finding roots in the NymPy library'''

    A = np.max(np.roots([1, 2 * p, p * p - 4 * r, q * q]))
    a = sqrt(A.real)

    # a - не может быть нулем исходя из самого метода.
    summand1 = p + a * a
    summand2 = q / a

    b = (summand1 - summand2) * 0.5
    c = (summand1 + summand2) * 0.5

    roots1 = [i + const3 for i in QuadraticTrinomials(1, a, b).complex_roots]
    roots2 = [i + const3 for i in QuadraticTrinomials(1, -a, c).complex_roots]
    return [roots1, roots2]
