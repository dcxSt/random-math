# distinct prime factors

from primeFactors import pfactors

def repete(someList):
    # if there is repetition in the list be angry
    b = someList[:]
    b.sort()
    for i in range(len(b)-1):
        if b[i]==b[i+1]:
            return True
    return False
a=input("lower bound: ")
b=input("upper bound: ")
a=int(a)
b=int(b)

haveDistinctPrimeFactors=[]
for n in range(a,b):
    factors=pfactors(n)
    if not repete(factors) and len(factors)!=1:
        haveDistinctPrimeFactors.append(n)
        print(n,":",factors,"\n")

print("\n\n\n",haveDistinctPrimeFactors)


