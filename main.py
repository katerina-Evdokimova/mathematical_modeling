from methods import Polynomials, bezout, solve, method_cardano_descartes

print(bezout(Polynomials(2, 6, 14, -42, -52)))  # [-1, 2, (-2+3j), (-2-3j)]
print(solve(Polynomials(2, 12, 18, 0)))  # (0.0, (-3+0j), (-3+0j))
print(method_cardano_descartes(Polynomials(2, 6, 14, -42, -52)))