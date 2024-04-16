#Lab5

import matplotlib.pyplot as plt
import numpy as np
import random 
import math 



'''
    plt.plot(order, y, linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(can)):
        y.append(4)
    plt.plot(can, y, linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(can1)):
        y.append(3)
    plt.plot(can1, y, linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(wait)):
        y.append(2)
    plt.plot(wait, y, linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(wait1)):
        y.append(1)
    plt.plot(wait1, y, linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='red', markersize=3)                
'''

    

'''
    #can1
    for i in L:
        z=random.expovariate(1)      
        sum_c+=z  
        can.append(sum_c)


    #can2
    for i in L:
        z=random.expovariate(1)        
        sum_c1+=z  
        can1.append(sum_c1)
    
    '''
    #wait1
'''
    for i in L:
        z=random.expovariate(1)        
        sum_c1+=z  
        can1.append(sum_c1)
    

    wait.append(can[1])
    wait.append(order[3])
    wait.append(can[2])
    wait.append(can1[1])
    wait.append(can1[2])
    wait.append(can[3])

    wait1.append(order[4])
    wait1.append(wait[3])
    wait1.append(order[6])
    wait1.append(wait[4])
    wait1.append(order[7])
    wait1.append(wait[5])


    ready.append(can[1])
    ready.append(can[2])
    ready.append(can[3])
    ready.append(can[4])

    k=0
    for i in order:
        if(k==5):
            bad.append(i)
            k=0
        k+=1
'''        
    

def two():
    L=10     #шт/год
    u=10     #шт/год 1 кан
    u1=30    #шт/год 2 кан

    order=[]
    can=[]
    can1=[]
    wait=[]
    wait1=[]

    can_s=True #зайнятo
    can1_s=True
    wait_s=True
    wait1_s=True


    ready=[]
    bad=[]

    order.append(0) #order[0]=0
    sum_ord=0
    sum_c=0
    sum_c1=0


    y=[]
    
    #order
    for i in range(L):
        z=random.expovariate(10)
        sum_ord+=z
        order.append(sum_ord)

    can.append(order[0])
    
    can1.append(order[1])
    
    can_iter=iter(can)
    can1_iter=iter(can1)

    sum_c+=can[0]
    sum_c1+=can1[0]

    z=random.expovariate(1)      
    sum_c+=z  
    can.append(sum_c)

    z=random.expovariate(1)      
    sum_c1+=z  
    can1.append(sum_c1)
    next(can_iter)
    next(can1_iter)

    
    length=0
    new_sum=0
    new1_sum=0


    new=next(can_iter)
    new_sum+=new
    new1=next(can1_iter)
    new1_sum+=new1
                        
    sum_c=new_sum
    sum_c1=new1_sum

    
    for i in order:
        length=i
        if(order.index(i)!=0 and order.index(i)!=1):   

            '''
            if(can_s==False):
                new=next(can_iter)
                new_sum+=new
                new1=next(can1_iter)
                new1_sum+=new1
            '''

                 
            if(length<new_sum and length<new1_sum):
                if(wait_s==True):
                    wait.append(length)
                    wait_s=False

                elif(wait1_s==True):
                    wait1.append(length)
                    wait1_s=False
                
                else:
                    bad.append(length)

            
            else:
                if(length>new_sum and length<new1_sum):
                    #
                    if(wait_s==False):
                        wait.append(new_sum)
                        wait_s=True

                        ready.append(new_sum)

                        #
                        z=random.expovariate(u)      
                        #sum_c+=z  
                        new_sum+=new
                        can.append(new_sum)

                        #new=next(can_iter)
                        


                    #
                    #wait.append(sum_c)
                    #wait_s=True
                    if(wait1_s==False):
                        wait_s=False
                        wait1.append(length)
                        ready.append(new_sum)
                        wait1_s=False
                    else:
                        can.append(length)
                        ready.append(new_sum)
                        #wait.append(length)
                        #wait_s=False

                        #!?
                        z=random.expovariate(u)    
                        new_sum+=new
                        can.append(new_sum)

                        '''
                        sum_c+=z  
                        can.append(sum_c)

                        new=next(can_iter)
                        new_sum+=new
                        '''

                elif(length>new1_sum and length<new_sum):
                    #
                    if(wait_s==False):
                        wait.append(new1_sum)
                        wait_s=True

                        ready.append(new1_sum)

                        #
                        new1_sum+=new1
                        can1.append(new1_sum)
                        '''
                        z=random.expovariate(u1)      
                        sum_c1+=z  
                        can1.append(sum_c1)

                        new1=next(can1_iter)
                        new1_sum+=new1
                        '''
                    #
                    #wait.append(sum_c1)
                    #wait_s=True
                    if(wait1_s==False):
                        wait_s=False
                        wait1.append(length)
                        ready.append(new1_sum)
                        wait1_s=False
                    else:
                        #wait.append(length)
                        #wait_s=False

                        can1.append(length)
                        ready.append(new1_sum)

                        #!?
                        z=random.expovariate(u)    
                        new1_sum+=new1
                        can1.append(new1_sum)

                        '''                        
                        z=random.expovariate(u1)      
                        sum_c1+=z  
                        can1.append(sum_c1)

                        new1=next(can1_iter)
                        new1_sum+=new1
                        '''
                
                else:
                    #
                    #if(sum_c<sum_c1):
                    if(new_sum<new1_sum):
                        #

                        if(wait_s==False):
                            wait.append(new_sum)
                            wait_s=True
                            if(wait1_s==False):
                                wait1.append(new_sum)
                                wait_s=False
                                #wait1_s=True
                                wait1.append(length)
                                #wait1_s=False
                            else:
                                wait1.append(length)
                                wait1_s=False
                        else:
                            can.append(length)
                            ready.append(new_sum)

                            #
                            z=random.expovariate(u)    
                            new_sum+=new
                            can.append(new_sum)
                            '''
                            z=random.expovariate(u)      
                            sum_c+=z  
                            can.append(sum_c)
                            new=next(can_iter)
                            new_sum+=new
                            '''

                        '''
                        if(wait_s==False):
                            wait.append(sum_c)
                            wait_s=True

                            ready.append(sum_c)

                            #
                            z=random.expovariate(u)      
                            sum_c+=z  
                            can.append(sum_c)

                            new=next(can_iter)
                            new_sum+=new
                        #
                        #wait.append(sum_c)
                        #wait_s=True
                        if(wait1_s==False):
                            wait_s=False
                            wait1.append(length)
                            ready.append(sum_c)
                            wait1_s=False
                        else:
                            wait.append(length)
                            wait_s=False  

                            #!?
                            z=random.expovariate(u)      
                            sum_c+=z  
                            can.append(sum_c)

                            new=next(can_iter)
                            new_sum+=new
                        #
                        '''


                    else:
                        #
                        if(wait_s==False):
                            wait.append(new1_sum)
                            wait_s=True
                            if(wait1_s==False):
                                wait1.append(new1_sum)
                                wait_s=False
                                #wait1_s=True
                                wait1.append(length)
                                #wait1_s=False
                            else:
                                wait1.append(length)
                                wait1_s=False
                        else:
                            can1.append(length)
                            ready.append(new1_sum)

                            #
                            z=random.expovariate(u)    
                            new1_sum+=new1
                            can1.append(new1_sum)
                            '''
                            z=random.expovariate(u1)      
                            sum_c1+=z  
                            can1.append(sum_c1)
                            new1=next(can1_iter)
                            new1_sum+=new1'''

                        '''
                        if(wait_s==False):
                            wait.append(sum_c1)
                            wait_s=True

                            ready.append(sum_c1)

                            #
                            z=random.expovariate(u1)      
                            sum_c1+=z  
                            can1.append(sum_c1)
                            new1=next(can1_iter)
                            new1_sum+=new1
                        #
                        if(wait1_s==False):
                            wait_s=False
                            wait1.append(length)
                            ready.append(sum_c1)
                            wait1_s=False
                        else:
                            wait.append(length)
                            wait_s=False  

                            #!?
                            z=random.expovariate(u1)      
                            sum_c1+=z  
                            can1.append(sum_c1)
                            new1=next(can1_iter)
                            new1_sum+=new1
                        '''


                '''
                z=random.expovariate(1)      
                sum_c+=z  
                can.append(sum_c)

                z=random.expovariate(3)      
                sum_c1+=z  
                can1.append(sum_c1)
                '''

    ready.append(can[-1])
    ready.append(can1[-1])                        

    print("Order: ")
    print(order)

    print("Can: ")
    print(can)
    print("Can1: ")
    print(can1)

    print("Wait: ")
    print(wait)
    print("Wait1: ")
    print(wait1)

    print("Ready: ")
    print(ready)
    print("Bad: ")
    print(bad)





    y=[]
    for i in range(len(bad)):
        y.append(1)
    plt.plot(bad, y, linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(ready)):
        y.append(2)
    plt.plot(ready, y, linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(wait1)):
        y.append(3)
    plt.plot(wait1, y, linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(wait)):
        y.append(4)
    plt.plot(wait, y, linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(can1)):
        y.append(5)
    plt.plot(can1, y, linewidth = 1, marker='o', markerfacecolor='red', markersize=3)   
    y=[]
    for i in range(len(can)):
        y.append(6)
    plt.plot(can, y, linewidth = 1, marker='o', markerfacecolor='red', markersize=3)
    y=[]
    for i in range(len(order)):
        y.append(7)
    plt.plot(order, y, linewidth = 1, marker='o', markerfacecolor='red', markersize=3)   


    plt.show()


    

two()