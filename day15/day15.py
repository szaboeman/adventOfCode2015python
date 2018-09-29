import sys
import re
def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data


def solvedAB(data):  
    values=[]
    maxvalue=0
    for i in range(1,100-2):      
        for j in range(1,100-i-1):
            for k in range(1,100-i-j):
                l=100-i-j-k
                sz=1
                for m in range(0,4):
                    v=(int(data[0][m])*i+int(data[1][m])*j+int(data[2][m])*k+int(data[3][m])*l)
                    if (v<0):
                        sz=sz*0
                    else:
                        sz=sz*v
                values.append(sz)
                if (int(data[0][4])*i+int(data[1][4])*j+int(data[2][4])*k+int(data[3][4])*l==500):
                    if (maxvalue<sz):
                        maxvalue=sz
    return(max(values),maxvalue)

def getInfo(data):  
    for i,adat in enumerate(data): 
        data[i]=re.findall(r"[+-]?[\d]",adat)
    return data

def main():
    data=readInput().split('\n')
    data=getInfo(data)
    print(solvedAB(data))  

main()