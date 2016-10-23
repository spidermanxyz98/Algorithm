#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:34:08 2016

@author: xinlin
"""
import numpy as np
import time
import matplotlib.pyplot as plt

def partition(A):
    n=len(A)
    if n>=2:
        k=np.random.randint(0,n-1)  #choose the piviot
        
        #move the piviot to the first element
        A[0], A[k] = A[k], A[0]
        
        i=0     #label the boundary
        for j in range(1,n):
            if A[0]>=A[j]:
                A[i+1], A[j] = A[j], A[i+1]
                i+=1
        #move the pivoit element to the right position
        A[i], A[0] = A[0], A[i]
    
        #partition the list
        if i>0 and i<j:
            left=A[0:i+1]
            right=A[i+1:n]
        elif i==0:
            left=A[0:1]
            right=A[1:n]
        elif i==j:
            left=A[0:n-1]
            right=A[n-1:n]
        return(left,right)
            
    else:
        return(None)
        
def quicksort(A):
    n=len(A)
    #A=list(A)
    if n>=2:
        (left,right)=partition(A)
        lsorted=quicksort(left)
        rsorted=quicksort(right)
        return(np.concatenate([lsorted,rsorted]))
    if n==1:
        return(A)
        
###Test the running time of quicksort
array_sizes=list((10**exp for exp in range(5,6)))
run_time_home=[]
#run_time_python=[]

for array_size in array_sizes:  
    test=np.random.random_integers(1, 10**7,array_size)
    start_time=time.time()
    result=quicksort(test)
    run_time_home.append(time.time()-start_time)
    
    #start_time=time.time()
    #result=np.sort(test)
    #run_time_python.append(time.time()-start_time)
    #print(array_sizes)
    #print('Time elapsed:',time.time()-start_time)
    #print(result[:10])
plt.figure(0)
plt.plot(array_sizes, run_time_home,"o", color='red')
#plt.plot(array_sizes, run_time_python, "o", color='green')

plt.xscale('log')
#plt.yscale('log')


#scale=list(map(lambda x:x*np.log(x), list(array_sizes)))
#plt.figure(1)
#plt.plot(array_sizes,scale,'o')
#plt.xscale('log')