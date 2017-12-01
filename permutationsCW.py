def permutationz(string):
	spList=[]
	perms=[]
	out=[]
	#print('in permutationz of ',string)
	for i in string:
		spList.append(i)
	spList.sort()
	#print('splist is',spList)
	#print('length of splist is ',len(spList))

	if(len(spList)>2):
		#print('in if')
		for i in range(0,len(spList),1):
			#print('splistfor is',spList)
			perms=[]
			for _j in spList:
				perms.append(_j)
			#print('perms is ',perms)
			perms.remove(perms[i])
			#print('removedperms is ',perms)
			#print('largersplist is ',spList)

			permstring=''
			for _k in perms:
				permstring=permstring+_k
			#print('perms is',perms)
			#print('permstring is ',permstring)
			#print('calling permutationzfor')
			temp=permutationz(permstring)
			for j in range(len(temp)):
				temp[j]=spList[i]+temp[j]
			out=out+temp
		return out
	elif(len(spList)<=1):
		return spList
	else:#len(splist==2)
		#print('in else')
		#print('else returning ',[string[0]+string[1],string[1]+string[0]])
		return [string[0]+string[1],string[1]+string[0]]
	#print(spList)

#print(len(['b','c']))
def permutations(str):
	return list(set(permutationz(str)))
	
x=permutations('abcad')
print(x)
y=(permutations('a'))
print(y)
z=list(set(permutationz('')))
print(z)