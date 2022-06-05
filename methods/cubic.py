import math

import numpy as np

from methods import Polynomials
from methods.checking_polynomial import checking

x = 1j * math.sqrt(3)
OMEGA1 = 0.5 * x - 0.5
OMEGA2 = -1.0 - OMEGA1
CONST_1_3 = 1 / 3.0


# The method implements the Cardano method for polynomials of the third degree with integer coefficients.
# (More information about the Cardano method is written in readme.md)
# The input is: a third degree polynomial (the data type is a polynomial).
# The output is: a list of roots.
def solve(polynomial: Polynomials):
    '''Polynomial(a3, a2, a1, a0)

        A polynomial of the third degree!!!'''

    # Checking
    flag, result = checking(polynomial, 3)
    if not flag:
        return result

    # Cardano's method
    a1 = polynomial[1]
    a2 = polynomial[2]

    const0 = a2 * CONST_1_3
    const = a2 * const0

    p = a1 - const
    q = polynomial[0] - const0 * (a1 - 2 * const * CONST_1_3)

    const2 = -q * 0.5
    const3 = p * CONST_1_3

    u = const2 * const2 + const3 * const3 * const3

    pow_ = math.sqrt(u)

    if u >= 0:
        determinator = np.cbrt(pow_)
        k0 = const2 + determinator
        k1 = const2 - determinator
    else:
        k0 = np.cbrt(const2 + pow_)
        k1 = np.cbrt(const2 - pow_)

    y0 = k0 + k1
    y1 = OMEGA1 * k0 + OMEGA2 * k1
    y2 = OMEGA2 * k0 + OMEGA1 * k1
    return y0 - const0, y1 - const0, y2 - const0
