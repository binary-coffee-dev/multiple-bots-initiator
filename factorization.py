#def factor(number):
#    primes = []
#    prime = 2
#    while prime * prime <= number:
#        while number % prime == 0:
#            primes.append(prime)
#            number //= prime
#        prime += 1
#    if number > 1:
#        primes.append(number)
#    return primes

import random
from math import gcd

def pow_(a, b, M):
	x = 1
	while(b > 0):
		if(b & 1):
			x = mul(x, a, M)
		a = mul(a, a, M)
		b >>= 1
	return x

def mul(a, b, mod):
    ret = 0
    while(True):
    	if(b == 0):
    		break
    	a %= mod
    	b %= mod
    	if(b & 1):
    		ret += a
    		if(ret >= mod):
    			ret -= mod
    	b >>= 1
    	a <<= 1
    	if(a >= mod):
    		a -= mod
    return ret

def mpow2(x, y, mod):
    ret = 1;
    while(y):
        if(y & 1): 
            ret = mul(ret, (int)(x), mod)
        y >>= 1
        x = mul((int)(x), (int)(x), mod)
    return ret % mod;

def isPrime(p):
    if(p == 2):
    	return 1
    if (p % 2 == 0):
    	return 0
    q = p - 1
    a = 0
    t = 0
    k = b = 0
    while(q % 2 == 0):
    	q >>= 1
    	k += 1
    for it in range(0, 2):
        a = random.randint(0, p) % (p - 4) + 2
        t = mpow2(a, q, p);
        b = ((t == 1) or (t == p - 1))
        for i in range(1, k):
       		if(b):
       			break
       		t = mul(t, t, p)
       		if(t == p - 1):
       			b = 1
        if(b == 0):
            return 0
    return 1

def pollard_rho(n, c):
    x = 2
    y = 2
    i = 1
    k = 2
    d = 0
    while(True):
        x = (mul(x, x, n) + c)
        if (x >= n):
        	x -= n
        d = gcd(x - y, n)
        if (d > 1):
        	return d
        if (i == k):
        	y = x
        	k <<= 1
        i += 1
    return n;

factors = []

def factoriza(n):
	if(n == 1):
		return

	if(isPrime((int)(n)) == True):
		factors.append((int)(n))
		return
	i = 2
	d = n
	while(True):
		if(d != n):
			break
		d = pollard_rho((int)(n), i)
		i += 1
	factoriza(d)
	factoriza((int)(n) // (int)(d))

def factor(n):
    factoriza(n)
    return factors
