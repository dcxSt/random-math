# generate pickle of all primes 

import numpy as np
import pickle as pkl
from CheckPrime import checkPrime

n=None
try: n = int(input('number: '))
except: n=int(10**8/2)

prime_numbers = [2,3]

for i in range(6,n,6):
    if i%6**7==0:print(i)#trace
    if checkPrime(i-1):
        prime_numbers.append(i-1)
    if checkPrime(i+1):
        prime_numbers.append(i+1)

prime_numbers = np.array(prime_numbers)
np.save('primes_below_'+str(n),prime_numbers)

