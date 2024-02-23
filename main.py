import random

def one():
    m = [[0,1,0,0,0,0],
         [0.2,0,0.8,0,0,0,],
         [0,0.4,0,0.6,0,0],
         [0,0,0.6,0,0.4,0],
         [0,0,0,0.8,0,0.2],
         [0,0,0,0,1,0]]

    k=0
    m1=[]
    sum=0
    for n in range(20):
        for i in m:
            for j in i:
                if(j==k):
                    m1[i]=m[j]
    
        for i in range(6):
            z = random.randint(0, 1)
            if ((z < m1[0]) and (z > 0)):
                sum+=0
            if ((z > m1[0]) and (z < m1[0]+m1[1])):
                sum+=1
            if ((z >  m1[0]+m1[1]) and (z < m1[0]+m1[1]+m1[2])):
                sum+=2
            if ((z > m1[0]+m1[1]+m1[2]) and (z < m1[0]+m1[1]+m1[2]+m1[3])):
                sum+=3
            if ((z > m1[0]+m1[1]+m1[2]+m1[3]) and (z < m1[0]+m1[1]+m1[2]+m1[3]+m1[4])):
                sum+=4
            if ((z > m1[0]+m1[1]+m1[2]+m1[3]+m1[4]) and (z < m1[0]+m1[1]+m1[2]+m1[3]+m1[4]+m1[5])):
                sum+=5
            if ((z > m1[0]+m1[1]+m1[2]+m1[3]+m1[4]+m1[5]) and (z < 1)):
                sum+=6
            print ("Sum: ",sum)
        k=sum
        sum=0

        
        


one()