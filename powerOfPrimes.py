# power of primes

from primeFactors import pfactors

def allSame(someList):
    someList.sort()
    if len(someList)==0:
        return False
    if someList[0] == someList[-1]:
        return True
    return False

a=input("lower: ")
b=input("upper: ")
a=int(a)
b=int(b)

powerOfPrimes=[]
for i in range(a,b):
    if allSame(pfactors(i)) and len(pfactors(i))!=1:
        powerOfPrimes.append(i)
        print(i,"\t")
        #print(i,":\t",pfactors(i))

print("\n\n",powerOfPrimes)
