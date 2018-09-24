import sys
import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solution(input_text):
    output = []
    digits = [int(ch) for ch in input_text]
    last_digit = digits[0]
    count = 1
    for digit in digits[1:]:
        if digit == last_digit:
            count += 1
        else:
            output.extend((count, last_digit))
            last_digit = digit
            count = 1
    output.extend((count, last_digit))
    output_text = "".join([str(digit) for digit in output])
    return output_text

def solvedAB(s, numb):     
    digits=[int(c) for c in s]
    for i in range(int(numb)):
        output=[]
        db=0
        lastDigit=digits[0]
        for j in range(len(digits)):
            if digits[j]==lastDigit:
                db+=1
            else:
                output.extend((db,lastDigit))
                db=1
                lastDigit=digits[j]
        output.extend((db,lastDigit))
        digits=output
    return len(digits)
        


def main():
    startString=readInput()
    print(solvedAB(startString, 40))
    print(solvedAB(startString, 50))

main()