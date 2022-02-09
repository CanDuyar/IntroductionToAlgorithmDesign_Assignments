# CAN DUYAR - 171044075 / dynamic programming algorithm that finds the maximum profit belonging to the most profitable cluster


def findMaxProf(keepProfits):

    count = keepProfits[0]
    getMax = keepProfits[0]
    size = len(keepProfits)
    for t in range(size-1):
        count = count + keepProfits[t+1]
        count = max(keepProfits[t+1], count)
        getMax = max(getMax, count)

    return getMax


if __name__ == "__main__":
    keepProfits = [3, -5, 2, 11, -8, 9, -5]
    print("Maximum Profit =", findMaxProf(keepProfits))
