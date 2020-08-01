def missingNumber(arr):
    n = len(arr)
    return n*(n+1)/2 - sum(arr)


def missingNumber(arr):
    return sum(range(len(arr))) - sum(arr)
