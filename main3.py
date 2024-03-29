#Lab5

import matplotlib.pyplot as plt
import numpy as np
import random 
import math 

def one():
    file = open('1.txt', 'r')
    text = file.read()
    t=[]
    t=text.split(' ')

    data=[]
    for i in t:
        data.append(float(i))

    y=[]
    for i in range(200):
        y.append(i)

    plt.title("Ex.1")
    plt.plot(data, y)
    plt.show()
    
def two():
    file = open('1.txt', 'r')
    text = file.read()
    t=[]
    t=text.split(' ')

    data=[]
    for i in t:
        data.append(float(i))
    data.sort()

    a=0
    for i in data:
        a+=i

    y=[]
    for i in range(200):
        y.append(i)

    a=a/200 #середнє арифметичне
    d=0 #дисперчія
    o=0 #середнє вибіркове
    d1=[]
    
    for i in data:
        d+=(i-a)**2
        d1.append(d)
        
    d=d/200
    o=math.sqrt(d)

    
    new=[]
    k=0

    for i in data:
        new.append(i-k)
        k=i

    L=[]
    k=0

    for i in new:
        L.append(1/i)
    print(" ",L)


    plt.title("Ex.2")
    plt.step(y,data)
    plt.plot(y,L)
    plt.show()

def three():
    Tk=100
    #t=0
    #N=0
    t=[]
    N=[]

    t1=0
    n=0
    k=0
    lam=0

    while(t1<=Tk):
        z=random.normalvariate(0,1)
        while(k<5):
            k+=1
            z1=random.normalvariate(0,1)
            lam+=z1**2

        if z>0:
            L=(-1/lam)*math.log(z)
            t1+=L
            n+=1
            t.append(t1)
            N.append(n)

    print(" ",t)

def four():
    lam=6
    k=9
    Tk=100

    t1=0
    t2=[]
    n=0

    while(t1<=Tk):
        z=random.normalvariate(0,1)
        if z>0:
            T=(-1/lam)*math.log(z)
            t1+=T
            n+=1
            if(n==k):
                t2.append(t1)
                n=0
            

    print("Ex.4")
    print(" ", t2)


four()