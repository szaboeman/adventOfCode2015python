import sys
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solved(data,a,b):
    reg={'a':a, 'b':b}
    i=0
    while (i<len(data)):
        if (data[i][0]=="hlf"):
            reg[data[i][1]]/=2
            i+=1
        elif (data[i][0]=="tpl"):
            reg[data[i][1]]*=3
            i+=1
        elif (data[i][0]=="inc"):
            reg[data[i][1]]+=1
            i+=1
        elif (data[i][0]=="jmp"):
            i+=int(data[i][1])
        elif (data[i][0]=="jie"):
            if (reg[data[i][1]]%2==0):
                i+=int(data[i][2])
            else:
                i+=1
        elif (data[i][0]=="jio"):
            if (reg[data[i][1]]==1):
                i+=int(data[i][2])
            else:
                i+=1
    return reg["b"]
        

def main():
    data=readInput().split('\n')
    for i in range(len(data)):
        data[i]=re.split(r" |, ",data[i])
    print(solved(data,0,0))
    print(solved(data,1,0))

main()