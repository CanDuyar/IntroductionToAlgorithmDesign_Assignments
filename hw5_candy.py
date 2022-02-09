import sys

# CAN DUYAR - 171044075 / a dynamic programming algorithm that finds the maximum obtainable value

def produceCandies(priceList, n):
    temp = []
    for t in range(n+1):
        temp.append(0)

    for i in range(1, n+1): # from bottom to top part for dynamic programming
        keepMax = -sys.maxsize
        for j in range(i):
             keepMax = max(keepMax, priceList[j] + temp[i-j-1])
        temp[i] = keepMax

    return temp[n]

# TEST
if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(prices)
    print("Maximum Obtainable value =",produceCandies(prices, size))
