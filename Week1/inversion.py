# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

def count_inv(input):
    n=len(input)
    if n==1:
        return(0, input)
    else:
        A=input[0:int(n/2)]
        B=input[int(n/2):]
        
        (r_A, A)=count_inv(A)
        (r_B, B)=count_inv(B)
        (r_C, C)=count_merge_inv(A,B)
        return(r_A+r_B+r_C, C)
        

def count_merge_inv(input_l, input_r):
    n_l=len(input_l)
    n_r=len(input_r)
    C=[]
    num_inv=0
    i=0
    j=0
    while(i<n_l and j<n_r):
        if input_l[i]<=input_r[j]:
            C.append(input_l[i])
            i+=1
        else:
            C.append(input_r[j])
            num_inv=num_inv + n_l-i
            j+=1
    if i==n_l:
        C=C+list(input_r[j:])
    elif j==n_r:
        C=C+list(input_l[i:])
    return(num_inv, C)
    
    
def brutal_force(input):
    inv_num =0
    n=len(input)
    for i in range(n):
        for j in range(i+1,n):
            if input[i]>input[j]:
                inv_num+=1
    return(inv_num)
                
            
file=open('IntegerArray.txt','r')
input=file.readlines()
input=list(filter(None,list(map(lambda x:x.strip(),input))))
input=list(map(lambda x:int(x),input))
#print('The original arrary is', input)

start_time=time.time()
[num_inv, sorted_array]=count_inv(input)
time_elapse=time.time()-start_time
print('The number is inversion is:',num_inv)
print('\nTime elapsed:', time_elapse)


start_time=time.time()
num_inv=brutal_force(input)
time_elapse=time().time-start_time
print('\nThe number is inversion is', num_inv)
print('\nTime elapsed(brutal force):', time_elapse)

        
#file2=open('test.txt','r')
#input=file2.readlines()
#input=list(filter(None,list(map(lambda x: x.strip(),input))))
#input=list(map(lambda x:int(x),input))
#num_inv=brutal_force(input)
#print(num_inv)  
    