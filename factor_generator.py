from random import randint
from factorization import Miller_Rabin

def isprime(n):
    if n <= 1:
        return False
    return Miller_Rabin((2, 3, 5, 7, 11, 13, 17, 31, 61, 73, 23), n) == True

def large(n):
    x = randint(1, n)
    while not isprime(x):
        x += 1
    return x

p0 = large(2**60)
p1 = large(2**60)
hard = p0 * p1

print("{} * {} = {}".format(p0, p1, hard))