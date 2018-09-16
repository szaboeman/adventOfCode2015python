#!/user/bin/env python3 -tt

# Imports
import sys
import os
import hashlib

# Global variables
infile="input2.txt"

def readInput():
    with open(infile) as file:
        data = file.read()
    file.close()
    return data

def solvedAB(hash,nullCount):
    i=0
    good=False
    nullString=""
    for i in range(nullCount): 
        nullString=nullString+"0"  
    print(nullString)
    while not good:
        message=hash+str(i)
        m=hashlib.md5()
        m.update(message.encode("utf-8"))
        new_hash=m.hexdigest()
        if new_hash[0:nullCount]==nullString:
            good=True
        i=i+1
    return i-1


def main():
    hash=readInput()
    #print(solvedAB(hash,5))
    print(solvedAB(hash,6))
    sys.exit(1)

# Main body
if __name__ == '__main__':
    main()
