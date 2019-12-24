# collatz investigation

import array as arr
import matplotlib.pyplot as plt
import numpy as np


# the collatz sequence works this way : you start with a number, if it's even you just divide by 2 and add one
# if it's odd you multiply by 3 and add 1

def collatz(n,display=False): # calculates collatz sequence of integer n
    count=1
    if not display:
        while n!=1:
            count+=1
            if n%2==0:
                n=int(n/2)
            else:
                n=int(n*3+1)
    else:
        print(count," : ",n)
        while n!=1:
            count+=1
            if n%2==0:
                n=int(n/2)
            else:
                n=int(n*3+1)
            print(count," : ",n)
    return count

def collatzBranch(n): # calculates collatz and return branch of tree array
    branch = arr.array("L",[n])
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        branch.append(n)
    return branch
    

def estimateEvenProbability():
    # calculates first few collatz sequences and estimates
    # at the relative amount of even numbers appearing
    return # not yet written

def plotDensityOfAppearence(n,upto):
    return

def collatzPrimes(n):
    # determines which number 
    return # dummy

def main():
    for i in range(4,100,5):
        input("\n\nenter to procede:")
        collatz(n=i,display=True)


main()

