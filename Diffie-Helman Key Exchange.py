import gmpy2

p = gmpy2.mpz(input())
g = gmpy2.mpz(input())

def bob_sends_alice(p, g):
	stateb = gmpy2.random_state(2)
	badd = gmpy2.mpz_random(stateb, 10**1000)
	b = badd + 10**999
	print(b)
	bfinal = gmpy2.powmod(g, b, p) 
	return (b, bfinal)

def alice_sends_bob(p, g):
	statea = gmpy2.random_state(5)
	aadd = gmpy2.mpz_random(statea, 10**1000)
	a = aadd + 10**999
	print(a)
	afinal = gmpy2.powmod(g, a, p) 
	return	(a, afinal)

def print_shared_secret_alice(B, a, p):
	mainvalalice = gmpy2.powmod(bfinal,a,p)
	print(mainvalalice)
	return
	

def print_shared_secret_bob(A, b, p):
	mainvalbob = gmpy2.powmod(afinal,b,p)
	print(mainvalbob)
	return
	


b,bfinal = bob_sends_alice(p,g)
a,afinal = alice_sends_bob(p,g)


print_shared_secret_alice(bfinal,a,p)
print_shared_secret_bob(afinal,b,p)			