import gmpy2

p = gmpy2.mpz(input())
q = gmpy2.mpz(input())

m = gmpy2.mpz(input())

def encrypt(p,q,m):
	n = gmpy2.mul(p,q)
	phi = gmpy2.mul(p-1, q-1)
	e = gmpy2.next_prime(q)
	d = gmpy2.invert(e,phi) 
	c = gmpy2.powmod(m, e, n) 
	print(c)
	print(e)
	print(d)
	print(n)
	return (c,e,d,n)

def decrypt(c,d,n):
	m = gmpy2.powmod(c,d,n)
	return m


ct,et,dt,nt = encrypt(p,q,m)
ans = decrypt(ct,dt,nt)
print(ans)
