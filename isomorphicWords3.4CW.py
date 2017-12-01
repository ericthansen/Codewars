def isomorph(a, b):
  # Happy coding!
  #what a mess - not clean or efficient, but done. Python 3.4 alphabetizing dictionaries makes this harder!
  if len(a) != len(b):
    return False
  d=[]
  e=[]
  for i in a:
    d.append([i,0])
  for i in b:
    e.append([i,0])
#  print('d is',d)
#  print('e is',e)

  for i in d:
    for j in d:
        if (i[0]==j[0]):
            i[1]=i[1]+1
  for i in e:
    for j in e:
        if (i[0]==j[0]):
            i[1]=i[1]+1
  #print(i)
  #print(j)


#  print('d is',d,'e is',e)


  #print(d,e)
#  print(d.values())
#  print(e.values())
  
  out=True
  for i in range(len(d)):
    if(d[i][1]==e[i][1]):
        pass
    else:
        out=False
  out2=True
  dic={}
  for i in range(len(d)):
    if(d[i][0] in dic.keys()):
        #check if consistent
        if(dic.get(d[i][0])==e[i][0]):
            pass
        else:
            out2=False
    else:
        dic[d[i][0]]=e[i][0]


  return (out and out2)
#  if(str((d.values()))==str((e.values()))):#removed sorted
#    #print('hotdog')
#    return True
#  else:
#    #print('baddog')
#    return False


print(isomorph('aab','ccd'))
print(isomorph('estate','dueled'))
print(isomorph('xxy','xyy'))
print(isomorph("RAMBUNCTIOUSLY", "THERMODYNAMICS"))

'''  rem=[]
  for i in d:
    if (d.get(i,0)==e.get(i,0)):
        print('appending',i)
        rem.append(i)
    else:
        if(d.get(i,0)>0 and e.get(i,0)>0):
           print('returning false due to',i)
           print(d)
           print(e.get(i,0))
           return False
        else:
            pass
  for i in rem:
    del d[i]
    del e[i]
    print('d is',d)
'''
#stuff
