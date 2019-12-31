import random
from math import gcd

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
    for it in range(0, 10):
        a = random.randint(1, p - 1)
        t = pow(a, q, p);
        b = (((int)(t) == 1) or ((int)(t) == (int)(p - 1)))
        for i in range(1, k):
       		if(b):
       			break
       		t = mul(t, (int)(t), p)
       		if((int)(t) == (int)(p - 1)):
       			b = 1
        if((int)(b) == 0):
            return 0
    return 1

def pollard_rho(n, a, c):
	x = 2
	y = 2
	d = 1
	while(d == 1):
		x = (a * x * x + c) % n
		y = (a * y * y + c) % n
		y = (a * y * y + c) % n
		d = gcd(abs(x - y), n)
		if(d == n):
			return 0
	return d


factors = []

def factoriza(n):
	if(isPrime((int)(n)) == True):
		factors.append((int)(n))
		return
	d = pollard_rho((int)(n), random.randint(1, 100), random.randint(3, 10000))
	while(d == 0):
		d = pollard_rho((int)(n), random.randint(1, 100), random.randint(3, 10000))
	factoriza((int)(d))
	factoriza((int)(n) // (int)(d))

def factor(n):
	if((int)(n) == 1):
		return factors
	factoriza(n)
	factors.sort()
	return factors
