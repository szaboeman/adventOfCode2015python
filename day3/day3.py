#!/user/bin/env python3 -tt
"""
Task:
http://adventofcode.com/2015/day/1
"""

# Imports
import sys
import os

# Global variables
infile="input.txt"

def readInput():
    with open(infile) as file:
        data = file.read()
    file.close()
    return data

def solvedA(steps):
    x,y=0,0
    pos=[]
    for i in range(len(steps)):
        if steps[i]=='^':
            x+=1
        elif steps[i]=='v':
            x-=1
        elif steps[i]=='>':
            y+=1
        else:
            y-=1
        if not([x,y] in pos):
            pos.append([x,y])        
    #for value in pos:
    #    print(value)
    return len(pos)


def solvedB(steps):
    xs,ys,xr,yr=0,0,0,0
    pos=[]
    for i in range(len(steps)):
        if i%2==0:
            if steps[i]=='^':
                xs+=1
            elif steps[i]=='v':
                xs-=1
            elif steps[i]=='>':
                ys+=1
            else:
                ys-=1
            if not([xs,ys] in pos):
                pos.append([xs,ys])
        else:
            if steps[i]=='^':
                xr+=1
            elif steps[i]=='v':
                xr-=1
            elif steps[i]=='>':
                yr+=1
            else:
                yr-=1
            if not([xr,yr] in pos):
                pos.append([xr,yr])
    #for value in pos:
    #    print(value)
    return len(pos)

def main():
    steps=readInput()
    print(solvedA(steps))
    print(solvedB(steps))
    sys.exit(1)



# Main body
if __name__ == '__main__':
    main()
