# this program draws quite a simple fractal

import turtle
import numpy as np

def start(x=-350,y=-350):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()

def normDist(mean,sigma):
    return np.random.normal(mean,sigma)

def newRatios(ratios,sigma=(0.5,0.5)): # randomises by normal distribution
    new=[]
    for i in ratios:
        x=normDist(i[0],sigma[0])
        y=normDist(i[1],sigma[1])
        new.append((x,y))
    return new

def draw(iterations=3,ratios=[(3.0,5.0),(3,-1),(3,5)],
corners=[(-350,-350),(350,350)],
randomness=(0.5,0.5)):
    standardRatios=ratios[:]
    sumx=ratios[0][0]+ratios[1][0]+ratios[2][0]
    sumy=ratios[0][1]+ratios[1][1]+ratios[2][1]
    # graphSize is the bottom left and top right coordinates
    # draws two bends that splice the thing in 3
    # it splits the line in 3 so i decide that it will split according do x coordinate
    # only, and to the ratios list
    """
    for now the ratio list gives a list of 3 relative chuncks of coordinate
    """
    """
    really what i want to give is a list of all the corners
    """
    yMagnifier=1.0
    for i in range(iterations):
        
        # can include this later the code is incoplete
        """
        yMagnifier*=1.1
        newCorners=[]
        for i in corners:
            newCorners.append((i[0],i[1]*yMagnifier))
        corners=newCorners[:]
        """

        # redefine the corners according to following algorythem
        newCorners=[]
        for i in range(len(corners)-1):
            ratios=newRatios(standardRatios) # randomises by normal distribution
            l=corners[i]
            r=corners[i+1]
            newCorners.append(l)
            c2x=l[0]+(r[0]-l[0])*ratios[0][0]/sumx
            c2y=l[1]+ratios[0][1]*(r[1]-l[1])/sumy
            l1=(c2x,c2y)
            newCorners.append(l1)
            c3x=l1[0]+ratios[1][0]*(r[0]-l[0])/sumx
            c3y=l1[1]+ratios[1][1]*(r[1]-l[1])/sumy
            l2=(c3x,c3y)
            newCorners.append(l2)
        newCorners.append(r)
        corners = newCorners[:]
    return corners

        



def main():
    turtle.speed(100)
    start(-350,-350)
    corners=draw(iterations=8,randomness=(0.5,1.6))
    for i in corners:
        turtle.setpos(i[0],i[1])
    


main()
input("\n\npress enter to exit")
