import sys
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def incStraight(data):
    isInc=False
    i=0
    while (not isInc and i<len(data)-2):
        isInc=(data[i]-2==data[i+1]-1 and data[i+1]-1==data[i+2])
        i+=1
    return isInc

def isContainIOL(data):

    return (ord('i') in data or ord('l') in data or ord('o') in data)

def idDoublePair(data):
    onePair=''
    i=0
    db=0
    while (db<2 and i<len(data)-1):
        if (data[i]==data[i+1] and data[i]!=onePair):
            db+=1
            onePair=data[i]
        i+=1
    return db>=2

def nextPassword(data):
    j=0
    data[j]+=1
    while (data[j]>ord('z')):
        data[j]=ord('a')
        j+=1
        data[j]+=1
    return data

def solvedAB(data,t):
    data=[ord(ch) for ch in data]
    data.reverse()
    if t=='B': 
        data=nextPassword(data)
    while not incStraight(data) or not idDoublePair(data) or isContainIOL(data):
        nextPassword(data)
    data.reverse()
    data=''.join(chr(i) for i in data)
    return data

        


def main():
    data=readInput()
    solutionA=solvedAB(data,"A")
    print(solutionA)
    print(solvedAB(solutionA,"B"))

main()