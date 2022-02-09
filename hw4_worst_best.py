import sys

# CAN DUYAR - 171044075 / solution of the worst and the best results problem based on divide-and-conquer

def worstBestResults(listSuccess, l, r, worst=sys.maxsize, best=-sys.maxsize):

    if l == r:
        if worst > listSuccess[r]:
            worst = listSuccess[r]
        if best < listSuccess[l]:
            best = listSuccess[l]
        return worst, best

    if r - l == 1:
        if listSuccess[l] >= listSuccess[r]:
            if worst > listSuccess[r]:
                worst = listSuccess[r]
            if best < listSuccess[l]:
                best = listSuccess[l]
        else:
            if worst > listSuccess[l]:
                worst = listSuccess[l]
            if best < listSuccess[r]:
                best = listSuccess[r]
        return worst, best
    mid = (l + r) // 2
    worst, best = worstBestResults(listSuccess, l, mid, worst, best)
    worst, best = worstBestResults(listSuccess, mid + 1, r, worst, best)
    return worst, best

if __name__ == '__main__':
    listSuccess = [13,7,9,11,20,8,2,15]
    length = len(listSuccess)
    (worst,best) = worstBestResults(listSuccess, 0, length - 1)

    print("The worst result:", worst)
    print("The best result:", best)
