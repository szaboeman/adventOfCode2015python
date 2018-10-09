
import sys
import itertools

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedA(data):  
    c=0
    for i in range(1,len(data)):
        perm=list(itertools.combinations(data, i))
        for p in perm:
            if sum(p)==150:
                c+=1
    return c

def solvedB(data):  
    good=False
    c=0
    for i in range(1,len(data)):
        perm=list(itertools.combinations(data, i))
        for p in perm:
            if sum(p)==150:
                good=True
                c+=1
        if good:
            return c

def convertToInt(data):
    for i,adat in enumerate(data):
        data[i]=int(adat)
    return data

def main():
    data=readInput().split('\n')
    data=sorted(convertToInt(data))
    #data=data[::-1]
    #data.reverse()
    print(solvedA(data))
    print(solvedB(data))
main()