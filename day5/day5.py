import sys

#715 too hight

infile="input.txt"

def readInput():
    file=open(infile)
    data=file.read()
    file.close()
    return data

def countVowels(s):
    db=0
    vowels=['a','e','i','o','u']
    for i in range(len(vowels)):
        db+=s.count(vowels[i])
    return db

def doubleLetters(s):
    i=0
    good=False
    while i<len(s)-1 and not good:
        good=(s[i]==s[i+1])
        i+=1
    return good

def noughtyLetters(s):
    isExist=False
    noughtyLetters=['ab','cd','pq','xy']
    for i in range(len(noughtyLetters)):
        isExist=isExist or (s.find(noughtyLetters[i])>=0)
    return isExist

def solvedA(data):
    db=0
    for s in data:
        if (countVowels(s)>=3 and not noughtyLetters(s)  and doubleLetters(s)):
            db+=1
            #print(s,countVowels(s),doubleLetters(s),noughtyLetters(s))
    return db


#51 is stuck
def repeatXyX(s):
    i=0
    good=False
    while i<len(s)-2 and not good:
        good=(s[i]==s[i+2]) 
        i+=1
    return good
def doubleLettersRepeat(s):
    i=0
    good=False
    while (i<len(s)-3 and not good):
        find_string=s[i:i+2]
        good=(s.find(find_string,i+2)>=0)
        i+=1
    return good


def solvedB(data):
    db=0
    for s in data:
        if (doubleLettersRepeat(s) and repeatXyX(s)):
            db+=1    
    return db

def main():
    data=readInput().split('\n')
    print(solvedA(data))
    print(solvedB(data))
    sys.exit(1)

main()