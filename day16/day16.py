
import sys
import re

MFCSAM = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data


def solvedA(data):  
    for row in data:
        c=0
        for adat in row.items():
            if (adat[0]!="Sue" and int(MFCSAM[adat[0]])==int(adat[1])):
                c+=1
        if (c==3):
            return list(row.items())[0][1]
    return 0

def solvedB(data):  
    for row in data:
        c=0
        for adat in row.items():
            if (adat[0]!="Sue"):
                #and int(MFCSAM[adat[0]])==int(adat[1]))
                if (adat[0]=="cats" or adat[0]=="trees"):
                    if int(MFCSAM[adat[0]])<int(adat[1]):
                        c+=1
                elif adat[0]=="pomeranians" or adat[0]=="goldfish":
                    if int(MFCSAM[adat[0]])>int(adat[1]):
                        c+=1
                elif int(MFCSAM[adat[0]])==int(adat[1]):
                    c+=1
        if (c==3):
            return list(row.items())[0][1]
    return 0

def getInfo(data):  
    for i,adat in enumerate(data): 
        #data[i]=re.findall(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)",adat)
        array=re.split(r"Sue |: |, ",adat)
        data[i]={}
        data[i]["Sue"]=array[1]
        for j in range(3):
            data[i][array[2*j+2]]=array[2*j+3]
    return data

def main():
    data=readInput().split('\n')
    data=getInfo(data)
    print(solvedA(data))
    print(solvedB(data))

main()