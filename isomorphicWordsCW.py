def isomorph(a, b):
  # Happy coding!
  d={}
  e={}
  for i in a:
    if(i in d.keys()):
        d[i]=d[i]+1
    else:
        d[i]=1
  for i in b:
    if(i in e.keys()):
        e[i]=e[i]+1
    else:
        e[i]=1
  print('d is',d,'e is',e)


  #print(d,e)
  print(d.values())
  print(e.values())
  
  if(str((d.values()))==str((e.values()))):#removed sorted
    #print('hotdog')
    return True
  else:
    #print('baddog')
    return False
#for i in 'abc':
#   print(i)

#isomorph('aab','ccd')
print(isomorph('estate','dueled'))
#print(isomorph('xxy','xyy'))
#print(isomorph("RAMBUNCTIOUSLY", "THERMODYNAMICS"))

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
