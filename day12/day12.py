import sys
import json

def readInput():
    with open("input.txt") as file:
        data = json.load(file)
    return data

def solvedA(data, red=False):
    if (isinstance(data,list)):
        return sum([solvedA(adat,red) for adat in data])
    elif (isinstance(data, dict)):
        if (not red or red and not "red" in data.values()):
            return sum([solvedA(adat,red) for adat in data.values()])
        else:
            return 0
    elif (isinstance(data, str)):
        return 0
    elif (isinstance(data, int)):
        return data

def main():
    data=readInput()
    print(solvedA(data, False))
    print(solvedA(data, True))
main()