import unittest
from factorization import naive_factorization
from factorization import rho_factorization


def prod(numbersArray):
    prod = 1
    for n in numbersArray:
        prod *= n
    return prod


class NaiveFactorizationTests(unittest.TestCase):
    def test_SmallPrimes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 97]
        for prime in primes:
            factors = naive_factorization(prime)
            self.assertEqual(1, len(factors))
            self.assertEqual(prime, factors[0])

    def test_SmallCompositeNumbers(self):
        numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 49, 121]
        for n in numbers:
            factors = naive_factorization(n)
            p = prod(factors)
            self.assertEqual(n, p)

    def test_CornerCases(self):
        numbers = [-2, -1, 0, 1]
        for n in numbers:
            factors = naive_factorization(n)
            self.assertEqual(0, len(factors))


class RhoFactorizationTests(unittest.TestCase):
    def test_SmallPrimes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 97]
        for prime in primes:
            factors = rho_factorization(prime)
            self.assertEqual(1, len(factors))
            self.assertEqual(prime, factors[0])

    def test_SmallCompositeNumbers(self):
        numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 49, 121]
        for n in numbers:
            factors = rho_factorization(n)
            p = prod(factors)
            self.assertEqual(n, p)

    def test_CornerCases(self):
        numbers = [-2, -1, 0, 1]
        for n in numbers:
            factors = rho_factorization(n)
            self.assertEqual(0, len(factors))


if __name__ == '__main__':
    unittest.main()