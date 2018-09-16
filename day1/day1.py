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

def solvedA(row):
    size = len(row)
    startc=0
    endc=0
    for i in range(size):
        if row[i]=='(':
            startc+=1
        else:
            endc+=1
    return (startc-endc)

def solvedB(row):
    size = len(row)
    db=0
    i=0
    while True:
        if row[i]=='(':
            db+=1
        else:
            db-=1
        if db<0:
            break;
        i+=1
    return i+1

def main():
    row = readInput()
    print(solvedA(row))
    print(solvedB(row))
    sys.exit(1)



# Main body
if __name__ == '__main__':
    main()
