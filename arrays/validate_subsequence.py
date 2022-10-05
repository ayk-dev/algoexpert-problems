def isValidSubsequence(array, sequence):
    if array == sequence:
        return True
    pos = 0
    for i in range(len(array)):
        if pos == len(sequence):
            break
        if array[i] == sequence[pos]:
            pos += 1
            continue
    if pos == len(sequence):
        return True
    return False
