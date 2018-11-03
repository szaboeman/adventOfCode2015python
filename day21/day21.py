import itertools
import sys
import re
# 121 - 201
class Item(object):
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

weapons = [ Item("Empty", 0, 0, 0),
            Item("Dagger", 8, 4, 0),
            Item("Shortsword", 10, 5, 0),
            Item("Warhammer", 25, 6, 0),
            Item("Longsword", 40, 7, 0),
            Item("Greataxe", 74, 8, 0) ]

armors = [ Item("Empty", 0, 0, 0),
           Item("Leather", 13, 0, 1),
           Item("Chainmail", 31, 0, 2),
           Item("Splintmail", 53, 0, 3),
           Item("Bandedmail", 75, 0, 4),
           Item("Platemail", 102, 0, 5) ]

rings = [ Item("Empty", 0, 0, 0),
          Item("Damage +1", 25, 1, 0),
          Item("Damage +2", 50, 2, 0),
          Item("Damage +3", 100, 3, 0),
          Item("Defense +1", 20, 0, 1),
          Item("Defense +2", 40, 0, 2),
          Item("Defense +3", 80, 0, 3) ]

class Gamer(object):
    def __init__(self, hit, damage, defense):
        self.hit = hit
        self.damage = damage
        self.defense = defense


def isWin(i,j,k,l):
    e=Gamer(103,9,2)
    m=Gamer(100,weapons[i].damage+rings[k].damage+rings[l].damage, armors[j].armor+rings[k].armor+rings[l].armor)
    while (e.hit>0 and m.hit>0 and (e.damage>m.defense or m.damage>e.defense)):
        if (m.hit>0):
            h=m.damage-e.defense
            if (h<0):
                h=0
            e.hit-=h
        if (e.hit>0):
            h=e.damage-m.defense
            if (h<0):
                h=0
            m.hit-=h
    return e.hit<=0

def allCase():
    minValue=1000
    maxValue=0
    for i in range(1,len(weapons)):
        for j in range(1,len(armors)):
            for k in range(len(rings)):
                for l in range(len(rings)):
                    if (k==0 or k!=0 and k!=l):
                        actValue=weapons[i].cost+armors[j].cost+rings[k].cost+rings[l].cost
                        if (isWin(i,j,k,l) and minValue>actValue):
                            minValue=actValue
                        if (not isWin(i,j,k,l) and maxValue<actValue):
                            maxValue=actValue
    return minValue, maxValue
    

def main():
    print(allCase())
main()