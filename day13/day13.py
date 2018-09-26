import sys
import re
import itertools

def readInput():
    with open("input_test.txt") as file:
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

def solvedA(data):   
    names=getNames(data)
    for p in list(itertools.permutations(names)):
        print(p)
    return data


def main():
    data=readInput().split('\n')
    data=getInfo(data)
    print(solvedA(data))

main()