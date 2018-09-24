import sys
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedA(data):     
    answer=0
    for string in data:
        originalLen=len(string)
        string=re.sub(r'^\"|\"$','',string)
        string=re.sub(r'\\\\|\\"|\\x[0-9a-f]{2}|\\[a-z]',':',string)
        answer=answer+originalLen-len(string)
    return answer

def solvedB(data):     
    answer=0
    for string in data:
        originalLen=len(string)
        string=re.sub(r'\\','::',string)
        string=re.sub(r'\"','\\\"',string)
        print(string)
        answer=answer+len(string)+2-originalLen
    return answer

 
def main():
    data=readInput().split('\n')
    print(solvedA(data))
    print(solvedB(data))

main()