# CAN DUYAR - 171044075 / solution of the number of reverse-ordered pairs problem based on divide-and-conquer

def mergePairs(pairs, keepList, l, m, r):
    x = l
    y = m + 1
    k = l
    numberOfinversions = 0
    while x <= m and y <= r:
        if pairs[x] <= pairs[y]:
            keepList[k] = pairs[x]
            k += 1
            x += 1
        else:
            keepList[k] = pairs[y]
            numberOfinversions += (m-x + 1)
            k += 1
            y += 1
    while x <= m:
        keepList[k] = pairs[x]
        k += 1
        x += 1

    while y <= r:
        keepList[k] = pairs[y]
        k += 1
        y += 1
    for turn in range(l, r + 1):
        pairs[turn] = keepList[turn]

    return numberOfinversions

def countReversed(pairs, keepList, l, r):

    numberOfinversions = 0
    if l < r:
        m = (l + r)//2
        numberOfinversions += countReversed(pairs, keepList,l, m)
        numberOfinversions += countReversed(pairs, keepList,m + 1, r)
        numberOfinversions += mergePairs(pairs, keepList, l, m, r)
    return numberOfinversions


# TEST
if __name__ == "__main__":
    pairs = [4, 5, 13, 2, 7]
    length = len(pairs)
    keepList = [0]*length
    result = countReversed(pairs, keepList, 0, length-1)


    print("The number of reverse-ordered pairs:", result)
