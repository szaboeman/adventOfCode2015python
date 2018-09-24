import sys
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedA(data):     
    print(data)
        


def main():
    startString=readInput()
    print(solvedA(startString))

main()