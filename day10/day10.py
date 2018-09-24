import sys
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedAB(s, numb):     
    digits=[int(c) for c in s]
    for i in range(int(numb)):
        output=[]
        db=0
        lastDigit=digits[0]
        for j in range(len(digits)):
            if digits[j]==lastDigit:
                db+=1
            else:
                output.extend((db,lastDigit))
                db=1
                lastDigit=digits[j]
        output.extend((db,lastDigit))
        digits=output
    return len(digits)
        


def main():
    startString=readInput()
    print(solvedAB(startString, 40))
    print(solvedAB(startString, 50))

main()