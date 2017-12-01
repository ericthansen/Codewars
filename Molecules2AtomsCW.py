'''
For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
'''
def parse_molecule (formula):
    dic={}
    stack=[]
    lparens=['{','[','(']
    rparens=['}',']',')']

    #print('formula is',formula)
    l=[]
    if len(formula)==0:
        return {}
    for i in formula:
        if(i.isdigit()==False):
            l.append(i)
        elif ((i.isdigit()) and not (l[-1]).isdigit()):
            l.append(i)
        else:
            l.append(l.pop()+i)
    #formula="".join(l)
    formula=l

    for i in formula:
        #print('top of i loop, i is',i)
        if i in lparens:
            try:
                top=stack.pop()
            except:
                top=[None,None]
            #if top of stack is a paren
            if(top in rparens): #top of stack is a right parenthesis
                temp=[]
                top=stack.pop()
                while(top not in lparens):
                    top[1]=top[1]*1
                    temp.append(top)
                    #print('appending to temp',top)
                    top=stack.pop()
                l=len(temp)
                for _ in range(l):
                    stack.append(temp.pop())
            elif(top!=[None,None]):
                stack.append(top)
            stack.append(i)
            #print('appending',i)
        elif(i in rparens):
            #right paren, stack and pop down with following digit-assumes every rparen will be followed with a digit - bc why else would you have parens?
            #unfortunately they put in rando parentheses sometimes...
            stack.append(i)
            #print('appending',i)
        elif(i.isdigit()):
            #it's a number
            #pop and add to dictionary?
            top=stack.pop()
            if(top in rparens): #top of stack is a right parenthesis
                temp=[]
                top=stack.pop()
                while(top not in lparens):
                    top[1]=top[1]*int(i)
                    temp.append(top)
                    #print('appending to temp',top)
                    top=stack.pop()
                l=len(temp)
                for _ in range(l):
                    stack.append(temp.pop())
                    #print('appending to stack')
            elif(top[0].isalpha()):#then top of stack contains an element
                top[1]=int(i)
                stack.append(top)
            else:
                print('number following something not right paren or element')
        elif(i.isalpha()):
            try:
                top=stack.pop()
            except:
                top=[None,None]
            #if top of stack is a paren
            if(top in rparens): #top of stack is a right parenthesis
                temp=[]
                top=stack.pop()
                while(top not in lparens):
                    top[1]=top[1]*1
                    temp.append(top)
                    #print('appending to temp',top)
                    top=stack.pop()
                l=len(temp)
                for _ in range(l):
                    stack.append(temp.pop())
            elif(top!=[None,None]):
                stack.append(top)

            #now go on with the current thingie    
            #it's a letter - check upper or lower
            if(i.upper()==i):#then it's uppercase
                #stack it
                stack.append([i,1])
                #print('appending',[i,1])
            else:#then it's lowercase
                #alter previous stacked letter
                x=stack.pop()
                x[0]=x[0]+i
                stack.append(x)
                #print('altering',[i,1],'to',[i,x[0]])
        #print('stack is',stack)
    #end for i
    #print('stack is',stack)
    lngth=len(stack)
    for j in range(lngth):
        top=stack.pop()
        if dic.get(top[0],None)!=None:
            dic[top[0]]=dic.get(top[0])+top[1]
        else:
            dic[top[0]]=top[1]
    #end for j
    return dic

#print(parse_molecule ('H2O'))
#print(parse_molecule('H2NO3'))
#print(parse_molecule('H2(N2O)3'))
#print(parse_molecule('K4[ON(SO3)2]2'))
# return {K: 4, O: 14, N: 2, S: 4}

#magnesium_hydroxide = 'Mg(OH)2'
#print(parse_molecule(magnesium_hydroxide))   # return {Mg: 1, O: 2, H: 2}
#test='Hg2(Hg2N3O)3'
#print(parse_molecule(test))

#print(parse_molecule('C6H12O6'))
print(parse_molecule('{[Co(NH3)4(OH)2]3Co}(SO4)3'))
