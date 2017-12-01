def spiralize(size):
    if(size==0):
        return []
    if(size==1):
        return [[1]]
    if(size==2):
        return [[1,1],[0,1]]
    if(size==3):
        return [[1,1,1],[0,0,1],[1,1,1]]
    if(size==4):
        return [[1,1,1,1],[0,0,0,1],[1,0,0,1],[1,1,1,1]]
    row=[None]*size
    for i in range(size):
        col=[0]*size
        row[i]=col
    spiral=row
    #print('spiral is',spiral)
    #markerposition
    xpos=0
    ypos=0
    #direction='r'
    #bounds
    rb=size-1
    lb=0
    ub=0+2
    bb=size-1
    #spiral[xpos][ypos]=1
    moved=True
    while(moved):
        moved=False
        movDist=0
        while(xpos<=rb):
            spiral[ypos][xpos]=1
            xpos+=1
            moved=True
            movDist+=1
        xpos-=1
        rb-=2
        if(movDist<=2):
            break

        movDist=0
        while(ypos<=bb):
            spiral[ypos][xpos]=1
            ypos+=1
            moved=True
            movDist+=1
        ypos-=1
        bb-=2
        if(movDist<=2):
            break

        movDist=0
        while(xpos>=lb):
            spiral[ypos][xpos]=1
            xpos-=1
            moved=True
            movDist+=1
        xpos+=1
        lb+=2
        if(movDist<=2):
            break

        movDist=0
        while(ypos>=ub):
            spiral[ypos][xpos]=1
            ypos-=1
            moved=True
            movDist+=1
        ypos+=1           
        ub+=2
        if(movDist<=2):
            break

        #print('spiral is',spiral)

    return spiral

x=spiralize(10)
for i in x:
    print(i)

#print(spiralize(8))
