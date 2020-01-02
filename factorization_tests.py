import unittest
from factorization import naive_factorization
from factorization import rho_factorization
from factorization import gnu_factor


def prod(numbersArray):
    prod = 1
    for n in numbersArray:
        prod *= n
    return prod

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


class NaiveFactorizationTests(unittest.TestCase):
    def test_SmallPrimes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 97]
        for prime in primes:
            assert(isPrime(prime))
            factors = naive_factorization(prime)
            self.assertEqual(1, len(factors))
            self.assertEqual(prime, factors[0])

    def test_SmallCompositeNumbers(self):
        numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 49, 121]
        for n in numbers:
            assert(not isPrime(n))
            factors = naive_factorization(n)
            self.assertTrue(all(isPrime(factor) for factor in factors))
            p = prod(factors)
            self.assertEqual(n, p)

    def test_CornerCases(self):
        numbers = [-2, -1, 0, 1]
        for n in numbers:
            factors = naive_factorization(n)
            self.assertEqual(0, len(factors))

    def test_LargePrimeNumbers(self):
        numbers = [30011, 2 ** 31 - 1, 68500657163]
        for n in numbers:
            factors = naive_factorization(n)
            self.assertEqual(1, len(factors))
            self.assertEqual(n, factors[0])

    def test_LargeCompositeNumbers(self):
        numbers = [30011 * 30011, 1009 * 200003]
        self.assertTrue(naive_factorization(numbers[0]) == [30011, 30011])
        self.assertTrue(naive_factorization(numbers[1]) == [1009, 200003])


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
            self.assertTrue(all(isPrime(factor) for factor in factors))
            self.assertEqual(n, p)

    def test_CornerCases(self):
        numbers = [-2, -1, 0, 1]
        for n in numbers:
            factors = rho_factorization(n)
            self.assertEqual(0, len(factors))

    def test_Range(self):
        for n in range(95000, 100000):
            r1 = naive_factorization(n)
            r2 = rho_factorization(n)
            r2.sort()
            self.assertTrue(r1 == r2)

    def test_LargeCompositeNumbers(self):
        numbers = [30011 * 19457058324883, 1009 * 200003 * 68500657163]
        self.assertTrue(naive_factorization(numbers[0]) == [30011, 19457058324883])
        self.assertTrue(naive_factorization(numbers[1]) == [1009, 200003, 68500657163])

class GNUFactorizationTests(unittest.TestCase):
    def test_SeveralNumbers(self):
        numbers = [30011 * 19457058324883, 1009 * 200003 * 68500657163, 2, 7]
        input = ' '.join(str(x) for x in numbers)
        output = gnu_factor(input)
        expected = str(numbers[0]) + ": 30011 19457058324883\n" + str(numbers[1]) + ": 1009 200003 68500657163\n2: 2\n7: 7\n"
        self.assertEqual(expected, output)
        

if __name__ == '__main__':
    unittest.main()