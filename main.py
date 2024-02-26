import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def f1(t,x,y):
    return 0

def f2(t,x,y):
    return 0

def one():
    x0=5
    y0=10
    t0=0
    tn=75
    a=0.1
    b=0.04
    c=0.3
    d=0.03
    h=0.5

    N=((tn-t0)/h)+1

    plt.rcParams["figure.figsize"] = (x0, y0)


    for t in range(75):
        xd=f1(t,x,y)
        yd=f2(t,x,y)
        

        x[t]=x[t-1]+h*xd
        y[t]=y[t-1]+h*yd

        t+=h

    plt.plot(x, y, linestyle="-", marker="o", label="X")
    plt.plot(x, y, linestyle="-", marker="o", label="Y")
    plt.legend()
    plt.show()

    

        
        


one()