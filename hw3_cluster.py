# CAN DUYAR - 171044075  / QUESTION 5

#5-a)
# BRUTE FORCE -> this method for part (a) of the question
def mostProfitableClusters(clusters):
       max = 0
       companies = []
       for g in range(0, len(clusters)):
           iter = 0
           for t in range(g, len(clusters)):
               iter = iter + clusters[t]
               if(iter > max):
                   max = iter
       for i in range(len(clusters)):
           sum = 0
           for j in range(i, len(clusters)):
               sum += clusters[j]
               if sum == max:
                   companies.append(clusters[i:j+1])
       return companies




#5-b)
# DIVIDE AND CONQUER -> this method for part (b) of the question
def maximumProfit(profitArray, l=None, r=None):

    left_iter = 0
    right_iter = 0
    summation = 0

    if len(profitArray) == 0:
        return 0

    if r is None and l is None:
        l = 0
        r = len(profitArray)-1

    if r == l:
        return profitArray[l]

    mid = (l + r) // 2

    for i in range(mid, l - 1, -1):
        summation = summation + profitArray[i]
        if summation > left_iter:
            left_iter = summation

    summation = 0

    for i in range(mid + 1, r + 1):
        summation = summation + profitArray[i]
        if summation > right_iter:
            right_iter = summation

    maxKeep = max(maximumProfit(profitArray, l, mid),
                    maximumProfit(profitArray, mid + 1, r))

    return max(maxKeep, left_iter + right_iter)



# TEST
if __name__ == "__main__":
    # BRUTE FORCE TEST for part a
    array = [3,-5,2,11,-8,9,-5]
    print("part a): ",mostProfitableClusters(array))
    #DIVIDE AND CONQUER TEST for part b
    print("part b): ",maximumProfit(array))
