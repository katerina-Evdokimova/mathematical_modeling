"""This module defines different types of Trinomials and their methods."""
from math import sqrt

from methods.Polynomials import FixedTermPolynomials, Monomials, Polynomials, FixedDegreePolynomials, Constants


class Trinomials(FixedTermPolynomials, valid_term_counts=(0, 1, 2, 3)):
    """Implements single-variable mathematical Trinomials."""

    def __init__(self,
                 Monomials1=None,
                 Monomials2=None,
                 Monomials3=None):
        """Initialize the Trinomials with 3 Monomials.

        The arguments can also be 2-tuples in the form:
            (coefficient, degree)
        """
        if not Monomials1:
            Monomials1 = Monomials(1, 1)
        if not Monomials2:
            Monomials2 = Monomials(1, 2)
        if not Monomials3:
            Monomials3 = Monomials(1, 3)
        args = [Monomials1, Monomials2, Monomials3]
        Polynomials.__init__(self, args, from_Monomialss=True)

    def __repr__(self):
        """Return repr(self)."""
        terms = self.terms
        assert len(terms) == 3
        t1, t2, t3 = terms
        return (
            "Trinomials(Monomials({0}, {1}), Monomials({2}, {3}), "
            "Monomials({4}, {5}))"
                .format(*t1, *t2, *t3)
        )


class QuadraticTrinomials(FixedDegreePolynomials, Trinomials, valid_degrees=2):
    """Implements quadratic Trinomialss and their related methods."""

    def __init__(self, a=1, b=1, c=1):
        """Initialize the Trinomials as ax^2 + bx + c."""
        if a == 0:
            raise ValueError("Object not a quadratic Trinomials since a==0!")
        Polynomials.__init__(self, a, b, c)

    @property
    def discriminant(self):
        """Return the discriminant of ax^2 + bx + c = 0."""
        c, b, a = self._vector
        return b * b - 4 * a * c

    @property
    def complex_roots(self):
        """Return a 2-tuple with the 2 complex roots of ax^2 + bx + c = 0.

        + root is first, - root is second.
        """
        c, b, a = self._vector
        D = b * b - 4 * a * c
        sqrtD = sqrt(D) if D >= 0 else sqrt(-D) * 1j
        a = a * 2
        const = 1 / a
        return (-b + sqrtD) * const, (-b - sqrtD) * const

    @property
    def real_roots(self):
        """Return a 2-tuple with the real roots if self.discriminant>=0.

        Return an empty tuple otherwise.
        """
        if self.discriminant < 0:
            return tuple()
        return self.complex_roots

    @property
    def complex_factors(self):
        """Return (a, (x-x_0), (x-x_1)), where x_0 and x_1 are the roots."""
        roots = self.complex_roots
        return (Constants(self.a),
                Polynomials([1, -roots[0]]),
                Polynomials([1, -roots[1]]))

    @property
    def real_factors(self):
        """Return (self,) if D < 0. Return the factors otherwise."""
        if self.discriminant < 0:
            return (self,)
        return self.complex_factors

    def __repr__(self):
        """Return repr(self)."""
        return (
            "QuadraticTrinomials({0!r}, {1!r}, {2!r})"
                .format(self.a, self.b, self.c)
        )
