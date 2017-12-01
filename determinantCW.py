def determinant(matrix):
    if(len(matrix)==1):
        return matrix[0][0]
    if(len(matrix)==2):
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    detTot=0
    for i in range(len(matrix)):
        iMinor=[]#dothis - #make minor matrix without 1st row/ithcol
        for j in range(len(matrix)):#iterate through columns
            if(j!=i):
                thisCol=[]
                for k in range(1,len(matrix),1):#iterate through rows
                    thisCol.append(matrix[j][k])
                #print(thisCol)
                iMinor.append(thisCol)
        #print(iMinor)

        curr=matrix[i][0]*determinant(iMinor)
        #print('curr is',curr)

        detTot=detTot+curr*(-1)**(i%2)#dothis
        #print('detTot is',detTot)
    return detTot


myl=[[1,2],[3,4]]
#print(myl[0][0])
x=determinant(myl)
#print(x)
myl2=[[1,2,3],[2,3,4],[3,4,5]]
#x2=determinant(myl2)
#print(x2)

m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant(m2))
#print(determinant(m2)==-20)

