import math

from methods import Polynomials
from methods.checking_polynomial import checking

x = 1j * math.sqrt(3)
OMEGA1 = (-1 + x) * 0.5
OMEGA2 = (-1 - x) * 0.5
CONST_1_3 = 1 / 3.0


# The method implements the Cardano method for polynomials of the third degree with integer coefficients.
# (More information about the Cardano method is written in readme.md)
# The input is: a third degree polynomial (the data type is a polynomial).
# The output is: a list of roots.
def solve(polynomial: Polynomials):
    flag, result = checking(polynomial, 3)
    if not flag:
        return result
    else:
        polynomial = result
    # Cardano's method
    const0 = polynomial[2] * CONST_1_3
    const = polynomial[2] * const0

    p = polynomial[1] - const
    q = polynomial[0] - const0 * (polynomial[1] - 2 * const * CONST_1_3)

    const2 = q * 0.5
    const3 = p * CONST_1_3
    u = const2 * const2 + const3 * const3 * const3
    pow_ = math.sqrt(u)

    if u >= 0:
        determinator = pow(pow_, CONST_1_3)
        k0 = -const2 + determinator
        k1 = -const2 - determinator
    else:
        k0 = pow((-const2 + pow_), CONST_1_3)
        k1 = pow((-const2 - pow_), CONST_1_3)

    y0 = k0 + k1
    y1 = OMEGA1 * k0 + OMEGA2 * k1
    y2 = OMEGA2 * k0 + OMEGA1 * k1
    return y0 - const0, y1 - const0, y2 - const0
