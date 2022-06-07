from methods import Polynomials, bezout, solve, method_cardano_descartes

print(bezout(Polynomials(1, 3, 7, -21, -26)))  # [-1, 2, (-2+3j), (-2-3j)]
print(solve(Polynomials(1, 6, 9, 0)))  # (0.0, (-3+0j), (-3+0j))
print(method_cardano_descartes(Polynomials(1, -4, -2, 21,
                                           -18)))  # [(-2.4085471216629553+0j), (-3.8126816011407194+0j), (1.1106143614018373+1.1841808874601647j), (1.1106143614018373-1.1841808874601647j)]
print(solve(Polynomials(2)))  # [1, -1, -1, -2.0]
