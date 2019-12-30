def factor(number):
    primes = []
    prime = 2
    while prime * prime <= number:
        while number % prime == 0:
            primes.append(prime)
            number //= prime
        prime += 1
    if number > 1:
        primes.append(number)
    return primes