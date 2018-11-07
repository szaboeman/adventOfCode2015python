import sys
import re
import itertools

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def multiply(inf):
    m=1
    for i in inf:
        m*=i
    return m 

def solvedA(data,group):
    goal=int(sum(data)/group)
    minimum=99999999999
    for i in range(1,7):
        for inf in itertools.combinations(data,i):
            if (sum(inf)==goal and minimum>multiply(inf)):
                minimum=multiply(inf)
    return minimum
        

def main():
    data=readInput().split('\n')
    data=[int(i) for i in data]
    print(solvedA(data,3))
    print(solvedA(data,4))

main()