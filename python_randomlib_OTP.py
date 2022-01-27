import random
a = 10**1023
b = 10**1024 - 1
finat = random.randint(a,b)   #gives us the 1023 digit number

newstr = str(finat)
otp = newstr[2:8]
finotp = int(otp)

print(finat)
print(finotp)
