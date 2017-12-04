#number and IP address
def numberAndIPaddress(s):
    if(s.count('.')==3):
        #then it's an ip address
        l=s.split('.')
        for i in range(len(l)):
            l[i]=str(bin(int(l[i]))[2:]).zfill(8)
            #print(l[i])
        x=int(l[0]+l[1]+l[2]+l[3],2)
        
    else:
        s=(bin(int(s))[2:]).zfill(32)
        #print('s:',s,'len s:',len(s))
        l=[0,0,0,0]
        l[0]=s[0:8]
        l[1]=s[8:16]
        l[2]=s[16:24]
        l[3]=s[24:32]
        x=''
        for i in range(len(l)):

            #print('li:',l[i],'int l[i]',int(l[i],2))

            x=x+str(int(l[i],2))+'.'
        x=x[0:-1]
    return str(x)

print(numberAndIPaddress('10.0.3.193'))#167773121
print(numberAndIPaddress('167969729'))#10.3.3.193

def tests():
    x='8'
    x=int(x)
    x=bin(x)[2:]
    print(x)
#tests()