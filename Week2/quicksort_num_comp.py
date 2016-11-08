#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:34:08 2016

@author: xinlin
"""
import numpy as np
import time
import matplotlib.pyplot as plt




#find the median amaong three elements
def find_median(a,b,c):
    if a>=b:
        if b>=c:
            return(b)
        elif a>=c:
            return(c)
        else:
            return(a)
    else:
        if a>=c:
            return(a)
        elif b>=c:
            return(c)
        else:
            return(b)



def partition(A):
    n=len(A)
    if n>=2:
        #k=np.random.randint(0,n-1)  #choose the piviot
        front=A[0]
        end=A[-1]
        if n%2 == 1:
            middle=A[int(np.floor(n/2))]
            piviot=find_median(front,end,middle)
        else:
            middle=A[int(n/2)-1]
        
        piviot=find_median(front,end,middle)
        
        if piviot==front:
            k=0
        elif piviot==end:
            k=n-1
        elif n%2 ==1:
            k=int(np.floor(n/2))
        else:
            k=int(n/2)-1
        print(k)
        #move the piviot to the first element
        A[0], A[k] = A[k], A[0]
        
        i=0     #label the boundary
        for j in range(1,n):
            if A[0]>=A[j]:
                A[i+1], A[j] = A[j], A[i+1]
                i+=1
        #move the pivoit element to the right position
        A[i], A[0] = A[0], A[i]
    
        return(i)    
    else:
        return(0)
        
counter=0  #counte the number of comparision (the sum of length(subarray)-1)

def quicksort(A):
    n=len(A)
    global counter
    if n>=2:
        counter+=n-1
        i=partition(A)
        #three cases after partition: 1.left array is zero 2. right array is zero
        #3.left and right arrays are non zero. 
        
        if i==0:
            quicksort(A[1:])
            return(A)
        elif i==n-1:
            quicksort(A[0:n-1])
            return(A)
        else:
            quicksort(A[0:i])
            quicksort(A[i+1:])
            return(A)
    if n==1:
        return(A)
        

        
        
file0=open('testarray.txt','r')
input0=file0.readlines()
input0=(filter(None, list(map(lambda x:x.strip(),input0))))
input0=list(map(lambda x:int(x),input0))
#print(input[-5:])       
        
        
        
file1=open('test1.txt','r')
input1=file1.readlines()
input1=(filter(None, list(map(lambda x:x.strip(),input1))))
input1=list(map(lambda x:int(x),input1))        
        
file2=open('test2.txt','r')
input2=file2.readlines()
input2=(filter(None, list(map(lambda x:x.strip(),input2))))
input2=list(map(lambda x:int(x),input2))      

file3=open('test3.txt','r')
input3=file3.readlines()
input3=(filter(None, list(map(lambda x:x.strip(),input3))))
input3=list(map(lambda x:int(x),input3))


quicksort(input0)



