from methods import Polynomials, bezout, solve, method_cardano_descartes

print(bezout(Polynomials(1, 3, 7, -21, -26)))  # [-1, 2, (-2+3j), (-2-3j)]
print(solve(Polynomials(1, 6, 9, 0)))  # (0.0, (-3+0j), (-3+0j))
print(method_cardano_descartes(Polynomials(1, -4, -2, 21, -18))) # [2, 3.0, -2.302775637731995, 1.3027756377319946]
print(solve(Polynomials(2)))  # [1, -1, -1, -2.0]
