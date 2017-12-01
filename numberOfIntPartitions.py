#global a 
#a=[None]*length
#a[1]=1
import math
def partitions(n):
    if(n>10000):
        return "error, n>10000 - this would take a while (>18 sec)"
    else:
    	sumDivs=[]
    	sumDivs.append(1)
    	for j in range(1,n+1,1):#make SumOfDivisor table
    		sumDivs.append(sumOfDiv(j))
    	#print("sumDivs is ",sumDivs)

    	parts=[]
    	parts.append(1)
    	for x in range(1,n+1,1):
    		temp=0
    		for k in range(0,x,1):
    			temp=temp+(sumDivs[x-k]*parts[k])
    			#print('parts[',k,'] is ',parts[k])
    			#print("temp is ",temp)
    		parts.append(temp/x)
    	#print('parts is ',parts)
    	return int(parts[n])
def sumOfDiv(n):
	s=0
	for i in range(1,n+1,1):
		if (n%i==0):
			s=s+i
	return s

    	
    		

#print(partitions(101))
#print('partitions(2) is ', partitions(2))
print('partitions(5) is', partitions(7))
#print('partitions(10) is', partitions(10))
#print('partitions(25) is', partitions(25))
#print('partitions(100) is ',partitions(100))
#print('partitions(10000) is ',partitions(10000))
#print('sumOfDiv(10) is ', sumOfDiv(10))

#1 
# 1,1  2
# 1 1 1  1,2  3
#1,1,1,1  1,1,2  2,2  1,3   4
#1x5  1112   122  113  14  23 5  