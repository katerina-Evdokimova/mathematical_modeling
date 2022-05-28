from cmath import sqrt

from core import Polynomial
from cubic import solve
from trinomial import QuadraticTrinomial


def _pow(a, k):
    p = 1
    while k > 0:
        if k & 1:
            p *= a
        a *= a
        k >>= 1
    return p


def method_cardano(polynomial: Polynomial):
    p = polynomial[2] - 3 * polynomial[3] * polynomial[3] \
        * 0.125
    r = polynomial[1] - polynomial[3] * polynomial[2] * 0.5 + polynomial[3] * polynomial[3] * polynomial[3] * 0.125
    q = polynomial[0] - polynomial[3] * polynomial[1] * 0.25 + polynomial[3] * polynomial[3] * polynomial[
        2] * 0.0625 - 3 * _pow(polynomial[3], 4) * 0.00390625
    A = solve(1, 2 * p, p * p - 4 * r, q * q)[0]
    a = sqrt(A).real
    b = (p + a * a - q / a) * 0.5
    c = (p + a * a + q / a) * 0.5

    roots1 = [i + polynomial[3] * 0.25 for i in QuadraticTrinomial(1, a, b).complex_roots]
    roots2 = [i + polynomial[3] * 0.25 for i in QuadraticTrinomial(1, -a, c).complex_roots]
    print(f'roots1 - {roots1}\ntoots2 - {roots2}')
