import sys

def readInput():
    with open("input_test.txt") as file:
        data = file.read()
    file.close()
    return data

def switch(table,mode, corner1, corner2):
    i=int(corner1[0])
    while (i<=int(corner2[0])):
        j=int(corner1[1])
        while (j<=int(corner2[1])):
            if (mode==2):
                table[i][j]=(table[i][j]+1)%2
            elif(mode==1):
                table[i][j]=1
            else:
                table[i][j]=0
            j+=1
        i+=1

def count1(table):
    db=0
    for i in range(1000):
        for j in range(1000):
            db+=table[i][j]
    return db

def solveA(data):
    table = []
    for i in range(1000):
        row =[]
        for j in range(1000):
            row.append(0)
        table.append(row)
    for row in data:
        inf=row.split(" ")
        if (inf[0]=="toggle"):
            corner1=inf[1].split(",")
            corner2=inf[3].split(",")
            switch(table,2,corner1, corner2)
        elif (inf[1]=="on"):
            corner1=inf[2].split(",")
            corner2=inf[4].split(",")
            switch(table,1,corner1, corner2)
        else:
            corner1=inf[2].split(",")
            corner2=inf[4].split(",")
            switch(table,0,corner1, corner2)
    return count1(table)

def switchB(table,mode, corner1, corner2):

    i=int(corner1[0])
    while (i<=int(corner2[0])):
        j=int(corner1[1])
        while (j<=int(corner2[1])):
            if (mode==2):
                table[i][j]+=2
            elif(mode==1):
                table[i][j]+=1
            else:
                table[i][j]-=1
                if table[i][j]<0: 
                    table[i][j]=0
            j+=1
        i+=1


def solveB(data):
    table = []
    for i in range(1000):
        row =[]
        for j in range(1000):
            row.append(0)
        table.append(row)
    for row in data:
        inf=row.split(" ")
        if (inf[0]=="toggle"):
            corner1=inf[1].split(",")
            corner2=inf[3].split(",")
            switchB(table,2,corner1, corner2)
        elif (inf[1]=="on"):
            corner1=inf[2].split(",")
            corner2=inf[4].split(",")
            switchB(table,1,corner1, corner2)
        else:
            corner1=inf[2].split(",")
            corner2=inf[4].split(",")
            switchB(table,0,corner1, corner2)
    return count1(table)


def main():
    data=readInput().split('\n')
    #print(solveA(data))
    print(solveB(data))
    print("Program vége")

main()