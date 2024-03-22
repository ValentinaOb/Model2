#Lab4
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


    plt.title("Ex.2")
    #plt.hist(data, y)
    plt.plot(y,d1)
    plt.show()

def three():
    l=100
    #t=0
    #N=0
    t=[l]
    N=[l]
    t[0]=0
    N[0]=0

    lam=8
    t1=0
    n=0
    

    while(n<=100):
        z=random.normalvariate(0,1)
        if z!=0:
            l=(-1/lam)*math.log(z)
        #t=t+l
        #N+=1
            t1+=l
            n+=1
            t.append(t1)
            N.append(n)
        #print(t)

    plt.plot(t,N)
    plt.title("Ex.3")
    plt.show()

three()