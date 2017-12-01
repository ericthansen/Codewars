def last_digit0(lst):
    etf=4
    zeros=[0]
    ones=[1]
    twos=[2,4,8,6]
    threes=[3,9,7,1]
    fours=[4,6,2,8]
    fives=[5,0]
    sixes=[6]
    sevens=[7,9,3,1]
    eights=[8,4,2,6]
    nines=[9,1]
    each=[zeros,ones,twos,threes,fours,fives,sixes,sevens,eights,nines]

    if(lst==[] or lst==[0,0]):
        return 1
    p=lst[len(lst)]
    b=lst[len(lst)-1]
    for i in range(len(lst)-2,-1,-1):
        if(p%4==0 and p!=0):
            effp=4
        else:
            effp=p%4
        print(effp)
        print('dig is',each[b][effp-1])

        p=each[b][effp-1]
        b=lst[i-2]

def last_digit2(lst):
    zeros=[0]
    ones=[1]
    twos=[2,4,8,6]
    threes=[3,9,7,1]
    fours=[4,6]
    fives=[5]
    sixes=[6]
    sevens=[7,9,3,1]
    eights=[8,4,2,6]
    nines=[9,1]
    each=[zeros,ones,twos,threes,fours,fives,sixes,sevens,eights,nines]
    etf=4#euler totient function phi(10)=4
    p=lst[len(lst)-1]%etf
    for i in range(len(lst)-1,0,-1):
        #print('i is',i)
        #b=(lst[i-1]%10)**p % 4
        #print('b is',b)
        #p=b
        #print('inloop p is',p)
        hi=lst[i]
        lo=lst[i-1]
        if(hi%etf==0):
            hi=etf
        else:
            hi=hi%etf
        curr=lo**hi
        lst[i-1]=curr
    #print('outloop p is',p)
    print('final answer is',lst[i-1]%10)

#last_digit2([12, 30, 21])
#last_digit2([3,3,3])
#last_digit2([2,2,4])
#last_digit2([123232, 694022, 140249])

#last_digit([3,3,3])

def last_digit3(lst):
    print('lst is',lst)
    if(lst==[] or lst==[0,0]):
        return 1
    elif(lst==[0,0,0]):
        return 0

    etf=4#euler totient function phi(10)=4; also bc any first digit has exponential congruence with period 4
    
    if(len(lst)==3):
        base=lst[0]%10
        #print('base is',base)
        mid=lst[1]
        hi=lst[2]
        if(mid%etf==0 and mid!=0):
            midP=etf
        elif(mid==0):
            midP=0
        else:
            midP=mid%etf
        #print('midP is',midP)
        midPP=(midP**hi)%etf
        if midPP==0: 
            midPP=etf
        if midP==0:
            if(hi==0):
                midPP=1
            else:
                midPP=0
        #print('midPP is',midPP)
        answer=base**midPP
        #print('  Answer is',answer%10)
        return answer%10
    elif(len(lst)==2):
        b=lst[0]%10
        p=lst[1]%4
        return (b**p)%10
    else:#lst is longer than 3
        x=lst[0:-1]
        #print('lst is',lst)
        #print('x is',x)
        x[-1]=x[-1]**lst[-1]
        return last_digit(x)

def last_digit(lst):
    etf=4
    zeros=[0,0,0,0]
    ones=[1,1,1,1]
    twos=[2,4,8,6]
    threes=[3,9,7,1]
    fours=[4,6,2,8]
    fives=[5,5,5,5]
    sixes=[6,6,6,6]
    sevens=[7,9,3,1]
    eights=[8,4,2,6]
    nines=[9,1,9,1]
    each=[zeros,ones,twos,threes,fours,fives,sixes,sevens,eights,nines]

    if(lst==[] or lst==[0,0]):
        return 1
    p=lst[len(lst)-1]
    b=lst[len(lst)-2]
    for i in range(len(lst)-2,-1,-1):
        b=b%4
        p=p%4+4*bool(n2)


'''print(last_digit([12, 30, 21]))#should be 6
print(last_digit([3,3,3]))#should be 7
print(last_digit([2,2,4]))#should be 6
print(last_digit([123232, 694022, 140249]))#should be 6
print(last_digit([499942, 898102, 846073]))#6
print(last_digit([937640, 767456, 981242]))#0
print(last_digit([0,0]))#1
print(last_digit([1,2]))#1
print(last_digit([1,2,1,1]))#1
print(last_digit([2,2,2,0]))#4
print(last_digit([2,0,1]))#1
print(last_digit([7, 6, 21]))#1
'''

print()
print()
print()
print()
print()

# ([7, 6, 21], 1)
x=21%4
print(x)
y=(6%4)**x
y2=(6%4)**21
print(y,'y2:',y2)
y2=y%4
print(y2)
z=7**y2
print(z)

def do():
    print(pow(504,500,10))

do()


'''
test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
'''

