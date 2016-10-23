# assume the len of the input is the power of 2 and there is no same element
import numpy as np
import time
def merge_sort(input):
	n=len(input)
	input=list(input)		#change the input to a list so that '+' can be used
	if n > 2:
		front=merge_sort(input[0:int(n/2)])
		back=merge_sort(input[int(n/2):])
		i=0
		j=0
		c=[]
		for k in range(0,n):
			if front[i] < back[j]:
				c.append(front[i])
				i+=1
			if i>len(front)-1:
				return(c+back[j:])
			if front[i] >= back[j]:
				c.append(back[j])
				j+=1
			if j>len(back)-1:
				return(c+front[i:])
	if n == 2:
		if input[0] > input[1]:
			return [input[1],input[0]]
		else:
			return input
			
	if n== 1:
		return input
		
def insertion_sort(input):
	input=list(input)
	n=len(input)
	for i in range(0,n):
		j=i
		while j>0 and input[j-1]>input[j]:
			temp=input[j]
			input[j]=input[j-1]
			input[j-1]=temp
			j-=1
	return(input)
	
def buble_sort(input):
	input=list(input)
	n=len(input)
	j=n
	while j>1:
		for i in range(0,j-1):
			if input[i]>input[i+1]:
				temp = input[i]
				input[i]=input[i+1]
				input[i+1]=temp
		j-=1
	return(input)

	

	
	
	
	
		
test=np.random.randint(1,1000000,1000000)
#test=[2,1,3,4,8, 6,5,10,11,18,20,59,23,56,78,31]
#print("original:\n")
#print(test)
#print("sorted:\n")		
#print(insertion_sort(test))
#print(buble_sort(test))
start_time=time.time()
merge_sort(test)
print("time elapsed (merge):{:10f}".format(time.time()-start_time))

start_time=time.time()
np.sort(test)
print("time elapsed (numpy.sort):{:10f}".format(time.time()-start_time))

#start_time=time.time()
#insertion_sort(test)
#print("time elapsed (insertion):{:10f}".format(time.time()-start_time))

#start_time=time.time()
#buble_sort(test)
#print("time elapsed (buble):{:10f}".format(time.time()-start_time))