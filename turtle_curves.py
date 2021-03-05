#!/home/steve/anaconda3/bin/python3

import turtle
import numpy as np
import math

turtle.speed(0)

def polarToCartesian(angle,r=450):
    x=math.cos(angle)*r
    y=math.sin(angle)*r
    return x,y

# %% ZOO OF CURVES

# lemniscate parameturised by phi, x=cos phi , y=sin 2phi
def lemniscate(phi):
    return (math.cos(phi)*400,math.sin(2*phi)*400)

def sinsandcoses(phi,k1=1.0,k2=7.3):
    return (math.sin(phi*k1)*400,math.cos(phi*k2)*400)

def polar_experiment1(phi):
    return (200 + 100*math.sin(14*phi) , phi + 0.1*math.sin(100.3*phi))

def polar_experiment1_1(phi):
    return (200 + 100*math.sin(14*phi) + 40*math.sin(5*phi) , phi + 0.04*math.sin(150.3*phi))

def polar_experiment1_2(phi):
    return (200 + 100*math.sin(14*phi) + 40*math.sin(5*phi) , 
            phi + 0.04*math.sin(150.3*phi)*(1-math.sqrt(abs(math.cos(0.11*phi)))))

def polar_experiment1_3(phi):
    j = abs(max(0,math.sin(14*phi)))**3
    return ((200 + 100*math.sin(14*phi) + 40*math.sin(5*phi) ) * (1 + j*0.02*math.cos(450.3*phi)) , 
            phi + j*0.02*math.sin(450.3*phi))

# %% DRAWING ETC.

# takes array of points in cartesian format and draws straight lines through them
def draw(arr):
    turtle.penup()
    turtle.setpos(arr[0][0],arr[0][1])
    turtle.pendown()
    for i in arr[1:]:
        turtle.setpos(i[0],i[1])
    return

def generate_line_arr(shape,length,grain):
    arr=[]
    for i in range(length):
        arr.append(shape(i*grain))
    return arr

def draw_cartesian(shape=lemniscate,grain="fine",length="standard"):
    graindic = {"very fine":0.0001 , "fine":0.001 , "standard":0.01, "coarse":0.1, "very coarse":1.0}
    g = graindic[grain]
    lengthdic = {"short":int(0.5/g) , "standard":int(5/g) , "long":int(50/g) , "super long":int(500/g)}
    l = lengthdic[length]
    arr = generate_line_arr(shape=shape,length=l,grain=g)
    draw(arr)
    return

def draw_polar(shape=polar_experiment1,grain="fine",length="standard"):
    graindic = {"very fine":0.0001 , "fine":0.001 , "okay":0.003 , "standard":0.01, "coarse":0.1, "very coarse":1.0}
    g = graindic[grain]
    lengthdic = {"short":int(0.5/g) , "standard":int(5/g), "long":int(50/g) , "super long":int(500/g)}
    l = lengthdic[length]
    arr = generate_line_arr(shape=shape,length=l,grain=g)
    arr2 = [(polarToCartesian(i[1],i[0])) for i in arr]
    draw(arr2)
    return

if __name__=="__main__":
    shape = polar_experiment1_1
    turtle.speed(0)
    #draw_cartesian(shape,grain="standard",length="long")
    draw_polar(shape,grain="okay",length="long")
    input("\n\nenter to exit")

