#!/home/steve/anaconda3/bin/python3

# modulo two times tables

import turtle
import numpy as np

def polarToCartesian(angle,r=450):
    x = np.cos(angle)*r
    y = np.sin(angle)*r
    return x,y

def findIntersection(pair1,pair2):
    # given 2 pairs of points which represent lines, find the intersection
    # if one or more of the lines is verticle
    if pair1[0][0] == pair1[1][0]:
        if pair2[0][0] == pair2[1][0]:
            return None # parallel or superimposed
        # y = a x + b
        a2 = (pair2[1][1]-pair2[0][1])/(pair2[1][0]-pair2[0][0])
        b2 = pair2[0][1]-a2*pair2[0][0]
        x=pair1[0][0]
        y=a2*x+b2
        return (x,y)

def draw(n=2,modulo=100,drawDots=False):
    turtle.speed(0)
    pairs=[]
    for i in range(modulo):
        j=i
        theta1 = j*2*np.pi/modulo
        theta2 = n*j*2*np.pi/modulo
        pair=[(polarToCartesian(theta1)),(polarToCartesian(theta2))]
        pairs.append(pair)
    if drawDots:
        for i in pairs:
            turtle.penup()
            turtle.setpos(i[0][0],i[0][1])
            turtle.dot()

    for i in pairs:
        turtle.penup()
        turtle.setpos(i[0][0],i[0][1])
        turtle.pendown()
        turtle.setpos(i[1][0],i[1][1])


"""
for i in range(2,30):
    a=False
    if i==2:
        a=True
    draw(n=i,modulo=100,drawDots=a)
    print("\n\npress enter to continue")"""
a=input("which number are you multiplying by?(try 51):")
a=int(a)
b=input("modulo what number (try 800):")
b=int(b)
draw(n=a,modulo=b,drawDots=False)

input("\n\npress enter to exit")

