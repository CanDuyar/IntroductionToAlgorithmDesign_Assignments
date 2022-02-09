# CAN DUYAR - 171044075 / Question 2

# first algorithm with Theta(N^2) time complexity
def polynomial_brute_force(P,x):
    t = 0.0
    for p in reversed(range(0,len(P))):
        degree = 1
        for g in range(1,p+1):
            degree = degree*x
        t = t + P[len(P)-p-1]*degree
    return t


# second algorithm(better) with Theta(N) time complexity
def polynomial_brute_force2(P,x):
    k = P[len(P)-1]
    degree = 1
    for g in range(1,len(P)):
        degree = degree*x
        k = k + P[len(P)-g-1]*degree
    return k


#TEST
if __name__ == "__main__":

    # first algorithm with Theta(N^2) time complexity
    # 2x^3 - 6x^2 + 2x - 1 for x = 3     =     5.0
    poly = [2, -6, 2, -1]
    x = 3
    print(polynomial_brute_force(poly,x))

    # second algorithm(better) with Theta(N) time complexity
    # 2x^3 + 3x + 1 for x = 2       =  23.0
    poly2 = [2, 0, 3, 1]
    x2 = 2
    print(float(polynomial_brute_force2(poly2,x2)))
