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
    with open(infile) as file: data = file.read()
    file.close()
    return data

def solvedA(rows):
    s=0
    for row in rows:
        data=row.split('x')
        t=[int(data[0])*int(data[1]),int(data[1])*int(data[2]),int(data[0])*int(data[2])]
        s+=2*sum(t)+min(t)
    return s

def solvedB(rows):
    s=0
    for row in rows:
        data=row.split('x')
        data=sorted(data, key=int)
        #print(data)
        s+=(2*(int(data[0])+int(data[1]))+int(data[0])*int(data[1])*int(data[2]))
    return s

def main():
    rows=readInput().split('\n')
    print(solvedA(rows))
    print(solvedB(rows))
    sys.exit(1)



# Main body
if __name__ == '__main__':
    main()
