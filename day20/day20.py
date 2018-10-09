
import sys
import math
#786240

def sumOfDealers(n):
    r=n+1
    o=2
    while o<=math.sqrt(n):
        if n%o==0:
            r=r+o+int(n/o)
        o+=1
    return r

def solvedA(n):
    i=n//45
    while sumOfDealers(i)<int(n/10):
        i+=1
    return i

def sumOfDealersB(n):
    r=n+1
    o=n//50
    while o<=n/2:
        if n%o==0:
            r=r+o
        o+=1
    return r

maxn=2000000
def solvedB(n):
    t=[0 for i in range(maxn)]
    for i in range(1,maxn//2):
        for j in range(1,51):
            if j*i<maxn:
                t[j*i]+=i*11
    i=0
    while i<maxn and t[i]<n:
        i+=1
    return i

        

def main():
    print(solvedA(34000000))
    print(solvedB(34000000))

main()