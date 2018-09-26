import sys
import re
def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def getDistance(row,ms):
    d=int(ms/(int(row[2])+int(row[3])))
    m=ms%(int(row[2])+int(row[3]))
    if (m>=int(row[2])):
        value=d*int(row[1])*int(row[2])+int(row[2])*int(row[1])
    else:
        value=d*int(row[1])*int(row[2])+m*int(row[1])
    return value


def solvedA(data,ms):   
    values=[]
    for row in data:
        values.append(getDistance(row,ms))
    return(max(values))

def solvedB(data,ms):  
    values=[] 
    for i in range(len(data)):
        values.append(0)
    for i in range(1,ms+1):
        distances=[]
        for row in data:
            distances.append(getDistance(row,i))
        
        index = [i for i, x in enumerate(distances) if x == max(distances)]
        for i in index:
            values[i]+=1        
    return max(values)
    

def getInfo(data):  
    for i,adat in enumerate(data): 
        data[i]=re.split(r" can fly | km/s for | seconds, but then must rest for",adat[0:len(adat)-9])
    return data

def main():
    data=readInput().split('\n')
    data=getInfo(data)
    print(solvedA(data,2503))
    print(solvedB(data,2503))

main()