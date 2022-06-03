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
        return 'error length polynomial < 3'
    if polynomial[3] != 1:
        polynomial /= polynomial[3]
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


print(solve(Polynomial(2, 12, 18, 0)))
