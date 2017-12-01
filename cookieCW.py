def cookie(x):
    try:
        if(x==True or x==False):
            return "Who ate the last cookie? It was the dog!"
        else:
            pass
    except:
        pass
    try:
        if(float(x)==x):
            return "Who ate the last cookie? It was Monica!"
        else:
            pass
    except:
        pass
    try:
        if(str(x)==x):
          return "Who ate the last cookie? It was Zach!"
        else:
            return "Who ate the last cookie? It was the dog!"
    except:
        return "Who ate the last cookie? It was the dog!"

def cookie2(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

def cookie3(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who

def cookie4(x=None):
    #print(type(x))
    if(x==''):
        who='the dog'
    if(type(x)==type(1) or type(x)==type(1.0)):
        who='Monica'
    elif(type(x)==type('s')):
        who='Zach'
    else:
        who='the dog'
    return "Who ate the last cookie4? It was %s!"%who

#print(type([1,2])==)
print(type(1.0)==type(2.0))
print(cookie4(1))
print(cookie4(1.0))
print(cookie4('1'))
print(cookie4(True))
print(cookie4(None))
print(cookie4())
print()

#print(cookie("Ryan"))
#print(cookie(2.3))
#print(cookie(26))
#print(cookie(True))
#print()

print(cookie2("Ryan"))
print(cookie2(2.3))
print(cookie2(26))
print(cookie2(True))
print()

print(cookie3("Ryan"))
print(cookie3(2.3))
print(cookie3(26))
print(cookie3(True))