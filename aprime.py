# a prime, gets user input for and prints wether that number is prime or not

from CheckPrime import checkPrime

keepGoing=True
while keepGoing:
    try:
        n = int(input("number you suspect is a prime: "))
        keepGoing=False
    except:
        pass
print(checkPrime(n))


