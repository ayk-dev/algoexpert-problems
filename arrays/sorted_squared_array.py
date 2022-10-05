def sortedSquaredArray(array):
    res = []
    for i in range(len(array)):
        res.append(array[i] * array[i])
    res.sort()
    return res
