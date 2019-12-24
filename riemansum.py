""" doing the integral of x^2 i found myself
trying to find how the sequence 

\lim_{n \to \infty} \sum_{i=1}^{n} \frac{i^2}{n^3}

"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
numerator=0
gs=[]
for i in range(1,200):
    numerator+=int(np.square(i))
    denom=int(np.power(i,3))
    print(i,"th number in the sequence")
    print("number as fraction: ",numerator,"/",denom)
    print("number as decimal: ",(numerator/denom))
    print("number as fraction of 1/3: ",((1/3)*denom/numerator))
    # now to compare this with 1/3rd we want to show what 1/3 is with the same denominator:
    k1= int(denom/3)
    k2=denom%3
    print("what 1/3rd looks like to us: ",k1,"R",k2,"/",denom)
    g=numerator-k1
    if k2==1:
        k2=2
        g-=1
    elif k2==2:
        k2=1
        g-=1
    print(g,"R",k2)
    g=g+k2/3
    gs.append(g)

    print()

plt.figure()

plt.plot(range(1,len(gs)+1),gs,"rx")

# fit a polynomial to it, do a taylor to like 5th order no more see where that gets you, try exponential

plt.show()
