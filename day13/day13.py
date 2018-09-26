import sys
import re
import itertools

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def getNames(data):
    nameList=[]
    for row in data:
        if not row[0] in nameList:
            nameList.append(row[0])
    return nameList


def getInfo(data):
    for i,row in enumerate(data):   
        data[i]=re.split(r" would | happiness units by sitting next to | ",row[0:len(row)-1])
    return data

def getValue(data, first, last):
    for row in data:
        if row[0]==first and row[3]==last:
            signum=-1
            if (row[1]=="gain"):
                signum=1
            return signum*int(row[2])

def solvedAB(data,me=False):   
    names=getNames(data)
    if me: 
        names.append("SzEm")
    values=[]
    for p in list(itertools.permutations(names)):
        sum=0
        for i in range(len(p)):
            if p[i]!="SzEm" and p[(i+1)%len(p)]!="SzEm":
                sum+=getValue(data,p[i],p[(i+1)%len(p)])
                sum+=getValue(data,p[(i+1)%len(p)],p[i])
        values.append(sum)
    return max(values)


def main():
    data=readInput().split('\n')
    data=getInfo(data)
    print(solvedAB(data))
    print(solvedAB(data,True))

main()