#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:27:43 2016

@author: xinlin
"""

#return the median of an array using insertion sort. Ths function is used for
#finding the median in the 5-element array. So insertion sort is fine.
import numpy as np

def median5(A):
    n=len(A)
    for j in np.arange(1,n):
        i=j-1
        while j>0 and A[j]<A[i]:
            A[j], A[i] = A[i], A[j]
            i-=1;
            j-=1
    return(A[int(np.ceil(n/2)-1)])
            

#takes the index of the piviot element. returns the index of the piviot in the
#sorted array. Also array A is partitioned into two parts with respect to the
#piviot
def partition(A,k):
    n=len(A)
    A[0], A[k] = A[k], A[0] 
    #i is labels the left most element that is larger than the piviot
    i=1
    for j in np.arange(1,n):
        if A[j]<A[0]:
            A[j], A[i]=A[i], A[j]
            i+=1
    A[0], A[i-1]=A[i-1], A[0]
    return(i-1)

    
        
    

def dselect(A,k):
    n=len(A)
    A=np.array(A)
    if n==1:
        return(A[0])
    
    subgroups=int(n/5)
    edgegroup=n%5
    
    #calcualate the median of medians
    c=[]
    for i in np.arange(subgroups):
        c.append(median5(A[5*i:5*(i+1)]))
    if edgegroup!=0:
        c.append(median5(A[5*subgroups:]))
    
    #recursively call dselect to find the median. Don't use median5 here (O(n^2))
    piviot=dselect(c,int(n/10))
    #np.where doesn't work for python list
    piviot_index, =np.where(A==piviot)

    i=partition(A,piviot_index)
    
    if i==k:
        return(piviot)
    elif i>k:
        return(dselect(A[:i],k))
    else:
        return(dselect(A[i+1:],k-i-1))





    