import math

from core import Polynomial

OMEGA1 = (-1 + 1j * math.sqrt(3)) * 0.5
OMEGA2 = (-1 - 1j * math.sqrt(3)) * 0.5
CONST_1_3 = 1 / 3.0


def solve(polynomial: Polynomial):
    """ Numeric solutions of a cubic equation
    a3 * x^3 + a2 * x^2 + a1 * x + a0 = 0
    """
    if len(polynomial) != 3:
        return 'error length polynomial < 4'
    if 0 < polynomial[3] != 1:
        polynomial /= polynomial[3]
    if polynomial[3] == 0:
        return ZeroDivisionError("Can't divide a Polynomial by 0")
    else:
        # Cardano's method
        p = polynomial[1] - (polynomial[2] * polynomial[2]) * CONST_1_3
        q = polynomial[0] - polynomial[1] * polynomial[2] * CONST_1_3 + (
                    2 * polynomial[2] * polynomial[2] * polynomial[2]) * CONST_1_3 * CONST_1_3 * CONST_1_3
        u = (q * 0.5) * (q * 0.5) + pow((p * CONST_1_3), 3)

        numerator = -q * 0.5
        if u >= 0:
            determinator = pow(u, 0.5 * CONST_1_3)
            k0 = numerator + determinator
            k1 = numerator - determinator
        else:
            pow_ = pow(u, 0.5)
            k0 = pow((numerator + pow_), CONST_1_3)
            k1 = pow((numerator - pow_), CONST_1_3)

        y0 = k0 + k1
        y1 = OMEGA1 * k0 + OMEGA2 * k1
        y2 = OMEGA2 * k0 + OMEGA1 * k1
        const = (polynomial[2] * CONST_1_3)
        return y0 - const, y1 - const, y2 - const


print(solve(Polynomial(1, 6, 9, 0)))
