import matplotlib.pyplot as plt
import numpy as np

def one():
    x0=5
    y0=15
    t0=0
    tn=150
    a=0.1
    b=0.04
    c=0.3
    d=0.03
    h=0.5
    N=((tn-t0)/h)+1

    x=[N]
    y=[N]
    t=[N]
    
    x[0]=x0
    y[0]=y0
    t[0]=t0
    k=0
    
    print(len(x))
    print(len(y))


    for i in range(int(N)):
        if(i!=0):
            xd=(a-b*y[i-1])*x[i-1]
            yd=(-c+d*x[i-1])*y[i-1]
            
            x.append(x[i-1]+h*xd)
            y.append(y[i-1]+h*yd)
            k+=h
            t.append(k)
            
    print(x)
    print("Y: ")
    print(y)
    print("T: ")
    print(t)

    plt.plot(t, x, label="Predator")
    plt.plot(t, y, label="Victim")
    plt.legend() 
    plt.show()
    

    

        
        


one()