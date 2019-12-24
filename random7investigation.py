# 1/2 divide by 7 random generator

import random

g=False
while not g:
    g=input(":")
    g=int(g)
    if g==0:
        g=True
    else:
        g=False
        n=random.randrange(10000)
        if random.choice([1,2])==1:
            n=int(int(n//7)*7)
        print(n)
input("\n\npress enter to exeunt")
