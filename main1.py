import matplotlib.pyplot as plt
import numpy as np
import random 
import math 

def one():
    x0=0
    t0=0
    tn=150
    h=0.5
    N=((tn-t0)/h)+1

    x=[N]
    x1=[N]
    x2=[N]
    x3=[N]
    x4=[N]
    x5=[N]
    x6=[N]
    x7=[N]
    x8=[N]
    x9=[N]

    f=[N]
    f1=[N]
    f[0]=0
    f1[0]=0
   
    t=[N]
    t1=[N]
    t2=[N]
    t3=[N]
    t4=[N]
    t5=[N]
    t6=[N]
    t7=[N]
    t8=[N]
    t9=[N]

    tf=[N]
    
    x[0]=x0
    x1[0]=x0
    x2[0]=x0
    x3[0]=x0
    x4[0]=x0
    x5[0]=x0
    x6[0]=x0
    x7[0]=x0
    x8[0]=x0
    x9[0]=x0

    t[0]=t0
    t1[0]=t0
    t2[0]=t0
    t3[0]=t0
    t4[0]=t0
    t5[0]=t0
    t6[0]=t0
    t7[0]=t0
    t8[0]=t0
    t9[0]=t0
    
    tf[0]=0
    k=0
    k1=2

    for j in range(10):
        for i in range(int(N)):
            if(k==tn): 
                k=0
                continue
            if(i!=0): 
                xd=((-1/2)*x[i-1]) + (((1-x[i-1]**2)**(1/2))*random.normalvariate(0, h))
                
                k+=h
                if(j==0):
                    x.append(x[i-1]+h*xd)
                    t.append(k)
                if(j==1):
                    x1.append(x1[i-1]+h*xd)
                    t1.append(k)
                if(j==2):
                    x2.append(x2[i-1]+h*xd)
                    t2.append(k)
                if(j==3):
                    x3.append(x3[i-1]+h*xd)
                    t3.append(k)
                if(j==4):
                    x4.append(x4[i-1]+h*xd)
                    t4.append(k)
                if(j==5):
                    x5.append(x5[i-1]+h*xd)
                    t5.append(k)
                if(j==6):
                    x6.append(x6[i-1]+h*xd)
                    t6.append(k)
                if(j==7):
                    x7.append(x7[i-1]+h*xd)
                    t7.append(k)
                if(j==8):
                    x8.append(x8[i-1]+h*xd)
                    t8.append(k)
                if(j==9):
                    x9.append(x9[i-1]+h*xd)
                    t9.append(k)


    for i in range(int(N)):
        if(i!=0 and i!=1): 
            ni=math.log(i)
            nu =math.log(ni)
            if(nu>0):
                fu=math.sqrt(2*i*nu)
                f.append(fu)
                f1.append(-fu)
                k1+=h
                tf.append(k1-2)
   

    plt.plot(t, x, label="x")
    plt.plot(t1, x1, label="x1")
    plt.plot(t2, x2, label="x2")
    plt.plot(t3, x3, label="x3")
    plt.plot(t4, x4, label="x4")
    plt.plot(t5, x5, label="x5")
    plt.plot(t6, x6, label="x6")
    plt.plot(t7, x7, label="x7")
    plt.plot(t8, x8, label="x8")
    plt.plot(t9, x9, label="x9")


    plt.plot(tf, f, label="f")
    plt.plot(tf, f1, label="f1")
    
    plt.show()

def two():
    
    N=1000
    St=[N]
    St[0]=10
    Wt=[N]
    Wt[0]=10

    '''
    St1=[N]
    St1[0]=10
    Wt1=[N]
    Wt1[0]=10

    St2=[N]
    St2[0]=10
    Wt2=[N]
    Wt2[0]=10

    St3=[N]
    St3[0]=10
    Wt3=[N]
    Wt3[0]=10
    '''

    h=0.01
    u =0.06
    o=0.1

    k=h
    t=[N]
    t[0]=h

    '''
    t1=[N]
    t1[0]=h
    
    t2=[N]
    t2[0]=h
    
    t3=[N]
    t3[0]=h
    '''

    for j in range(4):
        
        for i in range(N-1):
            if(i!=0):
                k+=h
                t.append(k)

                Wt.append(Wt[i-1]+random.normalvariate(0, h))
                St.append(St[i-1]*math.exp((u-((o*o)/2))*h+o*Wt[i]))

        plt.plot(t, St)
        St=[N]
        St[0]=10
        Wt=[N]
        Wt[0]=10
        t=[N]
        t[0]=h

    plt.legend(["S", "S1","S2","S3"])
    plt.show()

    
    '''
    k=h
    for i in range(N-1):
        if(i!=0):
            k+=h
            t1.append(k)

            Wt1.append(Wt1[i-1]+random.normalvariate(0, h))
            St1.append(St1[i-1]*math.exp((u-((o*o)/2))*h+o*Wt1[i]))
    k=h
    for i in range(N-1):
        if(i!=0):
            k+=h
            t2.append(k)

            Wt2.append(Wt2[i-1]+random.normalvariate(0, h))
            St2.append(St2[i-1]*math.exp((u-((o*o)/2))*h+o*Wt2[i]))
    k=h
    for i in range(N-1):
        if(i!=0):
            k+=h
            t3.append(k)

            Wt3.append(Wt3[i-1]+random.normalvariate(0, h))
            St3.append(St3[i-1]*math.exp((u-((o*o)/2))*h+o*Wt3[i]))
    '''
    '''
    plt.plot(t, St, label="S")
    
    
    plt.plot(t1, St1, label="S1")
    plt.plot(t2, St2, label="S2")
    plt.plot(t3, St3, label="S3")
    '''
    
def three():
    lam=8   
    N=10

    P=[N]
    P1=[N]
    t=[N]
    t[0]=0
    h=0
    h1=0

    for i in range(int(N)):
        h+=int(np.random.poisson(lam,1))
        h1+=int(np.random.poisson(lam,1))
        #P.append(math.exp(-lam*i)*(((lam*i)**k)/math.factorial(k)))
        
        P.append(h)
        P1.append(h1)
        t.append(i)

    plt.title("Ex.3")
    plt.step(P,t)
    plt.step(P1,t)
    plt.show()

 
def four():
    
    N=100
    St=[N]
    St[0]=10
    Wt=[N]
    Wt[0]=10


    h=0.01
    u =0.06
    o=0.1

    k=h
    t=[N]
    t[0]=h


    for j in range(25):        
        for i in range(N-1):
            while h!=4:
                if(i!=0):
                    k+=h
                    t.append(k)

                    Wt.append(Wt[i-1]+random.normalvariate(0, 4))
                    St.append(St[i-1]*math.exp((u-((o*o)/2))*h+o*Wt[i]))

        plt.plot(t, St)
        St=[N]
        St[0]=10
        Wt=[N]
        Wt[0]=10
        t=[N]
        t[0]=h

    #plt.legend(["S", "S1","S2","S3"])
    plt.title("Ex.4")
    plt.show()

    
    '''
    k=h
    for i in range(N-1):
        if(i!=0):
            k+=h
            t1.append(k)

            Wt1.append(Wt1[i-1]+random.normalvariate(0, h))
            St1.append(St1[i-1]*math.exp((u-((o*o)/2))*h+o*Wt1[i]))
    k=h
    for i in range(N-1):
        if(i!=0):
            k+=h
            t2.append(k)

            Wt2.append(Wt2[i-1]+random.normalvariate(0, h))
            St2.append(St2[i-1]*math.exp((u-((o*o)/2))*h+o*Wt2[i]))
    k=h
    for i in range(N-1):
        if(i!=0):
            k+=h
            t3.append(k)

            Wt3.append(Wt3[i-1]+random.normalvariate(0, h))
            St3.append(St3[i-1]*math.exp((u-((o*o)/2))*h+o*Wt3[i]))
    '''
    '''
    plt.plot(t, St, label="S")
    
    
    plt.plot(t1, St1, label="S1")
    plt.plot(t2, St2, label="S2")
    plt.plot(t3, St3, label="S3")
    '''
    

'''
n=int(input("N: "))
match n:
    case 1:
        one()
    case 2:
        two()
    case 3:
        three()

'''
three()
