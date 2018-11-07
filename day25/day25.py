import sys

def solved(row,col):
    level=col+((row+col-1)*(row+col-2))//2
    code=20151125
    for i in range(level-1):
        code=(code * 252533) % 33554393
    return code

def main():
    print(solved(2947,3029))

main()