
import sys
import itertools

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def neighbor(data,x,y):
    c=0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if (i>=0 and i<100 and j>=0 and j<100 and data[i][j]==1):
                if (i!=x or j!=y):
                    c+=1
    return c
def printT(data):
    for row in data:
        print(row)
    print("")

def solvedA(data):  
    for i in range(100):
        newTable=[]
        for j in range(100):
            newRow=[]
            for k in range(100):
                c=neighbor(data,j,k)
                if data[j][k]==1 and (c<2 or c>3):
                    newRow.append(0)
                elif data[j][k]==0 and c==3:
                    newRow.append(1)
                else:
                    newRow.append(data[j][k])
            newTable.append(newRow)
        data=newTable
    return sum(map(sum,data))

def solvedB(data):  
    for i in range(100):
        newTable=[]
        for j in range(100):
            newRow=[]
            for k in range(100):
                if not (k==0 and j==0 or k==0 and j==99 or k==99 and j==99 or k==99 and j==0):
                    c=neighbor(data,j,k)
                    if data[j][k]==1 and (c<2 or c>3):
                        newRow.append(0)
                    elif data[j][k]==0 and c==3:
                        newRow.append(1)
                    else:
                        newRow.append(data[j][k])
                else: 
                    newRow.append(data[j][k])
            newTable.append(newRow)
        data=newTable
    return sum(map(sum,data))

def getTable(data):
    newTable=[]
    for row in data:
        newRow=[]
        for c in row:
            if c==".":
                newRow.append(0)
            else:
                newRow.append(1)
        newTable.append(newRow)
    return newTable

def main():
    data=readInput().split('\n')
    data=getTable(data)
    print(solvedA(data))
    data[0][0]=1
    data[0][99]=1
    data[99][0]=1
    data[99][99]=1    
    print(solvedB(data))

main()