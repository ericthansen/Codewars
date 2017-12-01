import numbers
def move_zeros(array):
	ret=[0]*len(array)
	ind=0
	for x in array:
		try:
			if(isinstance(x,bool)==False and ((x*1)==0)):
				ind=ind
			else:
				ret[ind]=x
				ind=ind+1
		except TypeError:
			ret[ind]=x
			ind=ind+1
	return ret
			
#################################################################
a=[1,2,0,1,0,1,0,3,0,1]
#print(move_zeros(a))

b=["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
print(move_zeros(b))

c=[9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]
#print(move_zeros(c))
#print('False != 0 is', False!=0)
#print('False == 0 is', False==0)
#print('false == isinstance(False,numbers.integral) is ',isinstance(False,numbers.Integral))
print(isinstance( False, int ))
print(str(0.0))
print(False*1)
print((isinstance(None,bool)==False))
#print(None*1==0)