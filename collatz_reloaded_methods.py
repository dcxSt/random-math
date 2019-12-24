import matplotlib.pyplot as plt
import numpy as np

# takes input starting number, calculates collatz number, and also the number of even numbers and odd numbers appearing
def calculate_collatz(n, display=False):
    if display: print("Collatz n=",n)
    count,count_even,count_odd = 0,0,0
    while n!=1:
        count+=1
        if n%2==0:
            count_even+=1
            n/=2
        else:
            n*=3
            n+=1
            count_odd+=1
        n=int(n)
        if display:
            print(n,end="  ")
    return count,count_even,count_odd

def display_collatz1(n=100000):# default is one hundred thousand
    x = [i for i in range(1,k)]
    y = []
    for i in x:
        y.append(calculate_collatz(i,display=False))
    yt = np.transpose(y)

    # calculate ratios, odd divided by even is what I went for, else powers of two get infinity
    ratios = []
    for i in y:
        if i[1]!=0: ratios.append(i[2]/i[1])# odd divided by even
        else: ratios.append(0)

    # plot the figure
    plt.figure(figsize=(17,17))
    
    # plot the collatz number verses the generating natural number
    plt.subplot(2,2,1)
    plt.plot(x,yt[0],"bx")
    plt.title("the og collatz sequence")
    plt.ylabel("collatz number")
    plt.xlabel("n")
    plt.grid()

    # plot the even odd ratio, this should converge to something like 2/3
    plt.subplot(2,2,2)
    plt.plot(x,ratios,"rx")
    plt.ylabel("ratio")
    plt.xlabel("n")
    plt.title("odd divided by even")
    plt.grid()

    # plot the collatz number and the ratio
    plt.subplot(2,2,3)
    plt.plot(yt[0],[yt[2][i]/yt[1][i] for i in range(len(yt[1]))], "gx")
    plt.title("ratio by collatz number")
    plt.ylabel("ratio, odd divided by even")
    plt.xlabel("collatz number")
    plt.grid()

    # save figure
    if save_fig==True:
        plt.savefig("collatz_plot_xxx.png")





