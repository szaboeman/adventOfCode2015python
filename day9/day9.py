import sys
import re
import itertools

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def splitRow(data):
    for i,row in enumerate(data):   
        data[i]=re.split(r" to | = ",row)
    return data

def listCity(data):
    cities=[]
    for city in data:
        if not (city[0] in  cities):
            cities.append(city[0])
        if not (city[1] in  cities):
            cities.append(city[1])
    return cities

def solvedAB(routes):     
    cities=listCity(routes)
    values=[]
    for p in list(itertools.permutations(cities)):
        value=0
        for i in range(len(p)-1):
            j=0
            while not (routes[j][0]==p[i] and routes[j][1]==p[i+1] or
                   routes[j][0]==p[i+1] and routes[j][1]==p[i] ) and j<len(routes):
                   j+=1
            value+=int(routes[j][2])
        values.append(value)
    return min(values), max(values)
 


def main():
    data=readInput().split('\n')
    routes=splitRow(data)
    print(solvedAB(routes))

main()