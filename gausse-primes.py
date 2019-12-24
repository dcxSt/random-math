# gonna do what gausse did by hand when he was 14 years old and found
# that the primes decreased logarithmically

import numpy as np
import CheckPrime
import matplotlib.pyplot as plt


"""
the way this program works is there are 2 parameters:
- the size of the interval we are checking each time
- the number of intervals we will be checking
    The program will take no user input it's up to you to modify the
following 2 lines of code and play with the rest as you see fit
    I will then plot the things and hopefully find the logarithmic
relationsship he found by fitting and plotting the residuals and doing
a chi-squared test
"""


interval=10000
n=100
# a list to store the number of primes in each interval


def numberPrimes(low,high): # find the number of primes in the interval
    count=0
    for i in range(low,high):
        if CheckPrime.checkPrime(i):
            count+=1
    return count

def displayIntervals(interval,n,noPrimes):
    #plt.figure()
    high=int(interval*(n+1))
    try:
        plt.plot(np.linspace(interval,high,n),noPrimes,"bx-")
    except:
        print("Error"*100)
    
    # FUTURE WORK:
    # fit a line to it, plot the residuals
    # take the logerithem of each and plot those guys

    plt.show()

def saveResults(filename,interval,n,noPrimes):
    # becasue this takes ages to run i will save results to a text file
    f = open(filename,"w")
    f.write(str(interval))
    f.write("\n")
    f.write(str(n))
    f.write("\n")
    for i in noPrimes:
        f.write(str(i))
        f.write("\n")
    f.close()
    print("\nSaved")

def loadResults(filename): # returns interval,n,noPrimes
    try:
        f=open(filename,"r")
        interval=f.realine()
        print(interval)
        interval=int(interval)
        n=int(f.readline())
        noPrimes=[]
        i=f.readline()
        while i:
            i=int(i)
            noPrimes.append(i)
            i=f.readline()
        f.close()
        return interval,n,noPrimes
    except:
        print("\nError"*100)

def mode1(filename,interval,n): # calculate the primes etc. and save the result
    noPrimes=[]
    for i in range(n):
        b=numberPrimes(int(i*interval),int((i+1)*interval))
        noPrimes.append(b)

    # display the intervals using pyplot
    displayIntervals(interval,n,noPrimes)
    saveResults(filename,interval,n,noPrimes)

def mode2(filename): # loads the file and then displays it
    try:
        interval,n,noPrimes = loadResults(filename)
        displayIntervals(interval,n,noPrimes)
    except:
        print("Error\t\t"*100)
    


def main(filename,interval,n):
    #mode1(interval,n)
    mode2(filename)

    input("\n\nPress Enter to exit: ")
    
    

main("gausse-primes-data1.txt",interval,n)

input("press enter to exit")


