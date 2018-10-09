import itertools

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

print(findsubsets([5,5,5,10,15],4))