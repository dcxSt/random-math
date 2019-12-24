# all primes prints all primes within a specified range

from CheckPrime import checkPrime

keepGoing=True
while keepGoing:
    try:
        a = int(input("lower bound: "))
        b = int(input("upper bound: "))
        if a<b:
            keepGoing=False
    except:
        pass
count=0
for i in range(a,b):
    if checkPrime(i):
        count+=1
        print(i,end="\t")
        if count%10==0:
            print()
print()

