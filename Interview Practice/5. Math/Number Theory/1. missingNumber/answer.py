def missingNumber(arr):
    n = len(arr)
    return n*(n+1)/2 - sum(arr)

def missingNumber(arr):
    return sum(range(len(arr))) - sum(arr)

def missingNumber(arr):
    res = 0
    for i,v in enumerate(arr):
        res ^= (i + 1) ^ v
    return res