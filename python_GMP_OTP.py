import random
import gmpy2

#need random number of 1023 digits, and otp of 6 digits

state = gmpy2.random_state(34)
randest = gmpy2.mpz_random(state, 10**1023)
finalrand = randest + 10**1022

newstr = str(finalrand)
otp = newstr[4:10]
finalotp = int(otp)

print(finalrand)
print(finalotp)
