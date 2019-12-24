# prime factors utility class

from CheckPrime import checkPrime



def pfactors(n):
    primes=[]
    for i in range(2,n+1):
        if checkPrime(i):
            primes.append(i)
    factors=[]
    while n!=1:
        for i in primes:
            if n%i==0:
                factors.append(i)
                n=n/i
    return factors