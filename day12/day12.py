import sys
import json

def readInput():
    with open("input.txt") as file:
        data = json.load(file)
    file.close()
    print(data)
    return data

def solvedA(data):
   print(list(data.values())[0])


def main():
    data=readInput()
    solvedA(data)
main()