# test with fractal for the time series

import matplotlib.pyplot as plt
import numpy as np

"""
we can have 3 sine waves and then randomize the y and see what you get
we have an extra reallllllly big one with say 150 year period
first we have the big one with period of 11 years
then one that is much smaller and a final one
"""

def normDist(mean,sigma):
    # returns a random value normally distributed
    return np.random.normal(mean,sigma)

def getPeaks(n): # returns list of n points in time which are peaks in the Sn
    # the first one starts at zero
    peaks=[0]
    nextPeak=0
    for i in range(n-1):
        nextPeak+=np.random.normal(nextPeak+5.2,1.8) # these are kinda random values
        peaks.append(nextPeak)
    return peaks

def generateProbabilityDistribution(peaks):
    




