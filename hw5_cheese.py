# CAN DUYAR - 171044075 / a greedy algorithm that finds the maximum price you can get.

class Products:
    def __init__(self, weight, val, ind):
        self.cost = val // weight
        self.weight = weight
        self.ind = ind
        self.val = val

    def __lt__(self, other):
        return self.cost < other.cost

# greedy solution
class greedyMaxPrice:
    @staticmethod
    def maxGreedy(weight, val, cap):
        prods = []
        for u in range(len(weight)):
            prods.append(Products(weight[u], val[u], u))

        prods.sort(reverse=True)

        sum = 0
        for t in prods:
            keepValue = int(t.val)
            iterWeight = int(t.weight)
            if cap - iterWeight < 0:
                division = cap / iterWeight
                sum = sum + (keepValue * division)
                cap = int(cap - (iterWeight * division))
                break
            else:
                cap = cap - iterWeight
                sum = sum + keepValue

        return sum

# TEST
if __name__ == "__main__":
    weight = [10, 20, 30]
    val = [60, 100, 120]
    cap = 50

    maxValue = greedyMaxPrice.maxGreedy(weight, val, cap)
    print("Result =", maxValue)
