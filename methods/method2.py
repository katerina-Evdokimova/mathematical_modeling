from cmath import sqrt

# from Polynomials import Polynomials, QuadraticTrinomials
# from cubic import solve
from methods.Polynomials import Polynomials, QuadraticTrinomials
from methods.cubic import solve


def _pow(a, k):
    p = 1
    while k > 0:
        if k & 1:
            p *= a
        a *= a
        k >>= 1
    return p


def method_cardano_descartes(polynomial: Polynomials):
    if len(polynomial) != 4:
        return 'error length polynomial != 4'
    if polynomial[4] != 1:
        const = 1 / polynomial[4]
        polynomial *= const
    const = polynomial[3] * 0.125
    const2 = 3 * polynomial[3] * const
    p = polynomial[2] - const2
    r = polynomial[1] - polynomial[3] * (polynomial[2] * 0.5 + polynomial[3] * const)
    q = polynomial[0] - polynomial[3] * 0.25 * (polynomial[1] + polynomial[3] * 0.25 * (polynomial[2] - const2 * 0.5))
    A = solve(Polynomials(1, 2 * p, p * p - 4 * r, q * q))[0]
    a = sqrt(A).real
    # a - не может быть нулем исходя из самого метода.
    summand1 = p + a * a
    summand2 = q / a
    b = (summand1 - summand2) * 0.5
    c = (summand1 + summand2) * 0.5
    const = polynomial[3] * 0.25
    roots1 = [i + const for i in QuadraticTrinomials(1, a, b).complex_roots]
    roots2 = [i + const for i in QuadraticTrinomials(1, -a, c).complex_roots]
    return [roots1, roots2]
