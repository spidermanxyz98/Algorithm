#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:50:01 2016

@author: xinlin
"""
#This program is the first version of dselect.py. The mistakes here is that
#find_piviot recursively finds out the medians (not two times).
import numpy as np

#use insertion sort to find out the median element of the array with 5 elements
def find_meadian(A):
    n=len(A)
    for i in np.arange(1,n-1):
        j=i-1
        while j>=0 and A[i]<A[j]:
            A[i], A[j] = A[j], A[i]
            i-=1
            j-=1
    return(A[int((n-1)/2)])
    

#partition the array A with respect to the piviot (index) and return the index of the
#piviot element (the index start from zero)
def partition(A,piviot):
    n=len(A)
    if n==1:
        return(0)
    else:
        A[0], A[piviot]=A[piviot], A[0] 
        j=1
        for i in np.arange(1,n):
            if A[i]<=A[0]:
               A[j], A[i] = A[i], A[j]
               j+=1
        A[j-1], A[0] = A[0], A[j-1]
    return(j-1)
    

#return the meadian of medians of an array    
def find_piviot(A):
    n=len(A)
    if n==1:
        return(A[0])
    elif n<=5:
        return(find_meadian(A))
    else:
        #store the the medians of subgroups to a list C
        c=[]
        for i in np.arange(0, n, 5):
            if i < n-n%5:
                c.append(find_meadian(A[i:i+5]))
            else:
                c.append(find_meadian(A[i:]))
        return(find_meadian(c))

        
        
def quickselect(A,index):
    n=len(A)
    A=np.array(A)
    #find the piviot element
    if n==1:
        return(A[0])
    else:
        piviot=find_piviot(A)
        #find the the index of the piviot element
        k=np.where(A==piviot)[0][0]

        i=partition(A,k)
        if i==index:
            return(A[i])
        elif i>index:
            return(quickselect(A[0:i],index))
        else:
            return(quickselect(A[i+1:],index-i-1)) #carefully check shows that 
                                                   #there should be a 1 here!
    
    

               
