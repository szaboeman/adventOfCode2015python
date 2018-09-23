import sys
import re
from collections import deque

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedAB(data, type):
    wires={}
    for row in data:
        for value in row:
            if (value not in ("AND","OR","->","LSHIFT","RSHIFT","NOT")):
                if (not value.isnumeric()):
                    if value not in wires.keys():
                        wires[value]=''
        if (row[0].isnumeric() and len(row)==3):
            wires[row[2]]=row[0]
    if (type=='B'):  wires['b']=46065

    queue=deque(data)
    while (queue):
        row=queue.popleft()
        if (len(row)==4):
            if (wires[row[1]]!='') : 
                wires[row[3]]=~int(wires[row[1]])
            else: 
                queue.append(row)
        elif (len(row)==3):
            if (row[0].isnumeric() or wires[row[0]]!='') : 
                if (not row[0].isnumeric()):
                    wires[row[2]]=wires[row[0]]
            else:
                queue.append(row)
        elif (len(row)==5):
            if ((row[0].isnumeric() or wires[row[0]]!='') and 
                (row[2].isnumeric() or wires[row[2]]!='')):
                if (row[0].isnumeric()):
                    left=int(row[0])
                else:
                    left=int(wires[row[0]])
                
                if (row[2].isnumeric()):
                    right=int(row[2])
                else:
                    right=int(wires[row[2]])
                
                if (row[1]=='AND'):
                    wires[row[4]]=left & right
                elif(row[1]=='OR'):
                    wires[row[4]]=left | right
                elif(row[1]=='RSHIFT'):
                    wires[row[4]]=left >> right
                elif(row[1]=='LSHIFT'):
                    wires[row[4]]=left << right
            else:
                queue.append(row)
    return(wires['a'])
            



def main():
    data=readInput().split('\n')
    wires=[]
    for row in data: wires.append(row.split(" "))
    print(solvedAB(wires,'A'))
    print(solvedAB(wires,'B'))

main()