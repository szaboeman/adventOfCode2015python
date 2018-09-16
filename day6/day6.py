import sys
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data


def solvedAB(task,data):
    table = []
    for i in range(1000):
        row =[]
        for j in range(1000):
            row.append(0)
        table.append(row)
    for row in data:
        inf=re.split("(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)",row)
        for i in range(inf.count('')): 
            inf.remove('')
        # print(inf)
        for i in range(int(inf[1]), int(inf[3])+1):
            for j in range(int(inf[2]), int(inf[4])+1):
                if inf[0]=="toggle":
                    if task=='A':
                        table[i][j]=(table[i][j]+1)%2
                    else:
                        table[i][j]+=2
                elif inf[0]=="turn on":
                    if task=='A':
                        table[i][j]=1
                    else:
                        table[i][j]+=1
                else:
                    if task=='A':
                        table[i][j]=0
                    else:
                        table[i][j]-=1
                        if table[i][j]<0: table[i][j]=0
    return sum(map(sum,table))


def main():
    data=readInput().split('\n')
    print(solvedAB('A',data))
    print(solvedAB('B',data))
    print("Program vége")

main()