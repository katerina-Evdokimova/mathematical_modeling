from methods import Polynomials, bezout, solve, method_cardano_descartes

print(bezout(Polynomials(1, 3, 7, -21, -26)))  # [-1, 2, (-2+3j), (-2-3j)]
print(solve(Polynomials(1, 6, 9, 0)))  # (0.0, (-3+0j), (-3+0j))
print(method_cardano_descartes(Polynomials(1, 3, 7, -21, -26)))
# print(solve(Polynomials(1, 0.5, 0.25, 0.125)))

