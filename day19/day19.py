import sys
import math
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def splitData(data):
    vector=[]
    for i in range(len(data)-2):
        vector.append(data[i].split(' => '))
    return vector, data[-1]

def findAndReplace(baseString, math, replace):
    ind=[m.start() for m in re.finditer(math, baseString)]
    return [baseString[:i]+replace+baseString[i+len(math):] for i in ind]

def solvedA(data,string):
    molecules=set()
    for row in data:
        molecules.update(findAndReplace(string,row[0],row[1]))
    return len(molecules)


def solvedB(data, string):
    data.sort(key=lambda x: len(x[1]), reverse=True)
    steps=0
    while string!='e':
        swap=0
        for row in data:
            if (row[1] in string):
                string=string.replace(row[1], row[0], 1)
                print(string)
                steps+=1
                swap+=1
        if (swap==0): 
            break
        print(len(string))
    return steps       

def main():
    data=readInput()
    data, string=splitData(data.split('\n'))
    print(solvedA(data,string)) 
    print(solvedB(data,string))

main()