# print primes

def checkPrime(n): # boolean
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(3,int(n/2),2):
        if n%i == 0:
            return False
    return True

count=0
for n in range(3,100):
    if checkPrime(n):
        count+=1
        print(n,end="\t")
        if count%10==0:
            print()

input("\n\nPress enter to exit")
