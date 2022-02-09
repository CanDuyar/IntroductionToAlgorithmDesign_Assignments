# CAN DUYAR - 171044075 / a brute-force algorithm and a divide-and-conquer algorithm to solve the exponentiation problem

# brute force function
def expoBF(a,n):
    bf = 1
    for t in range(0,n):
        bf = bf * a
    return bf;


# divide & Conquer function
def expoDC(a,n):
    if(a == 0):
        return 0
    if(n < 1):
        return 1
    if(n%2 == 0):
        return expoDC(a*a, n/2)
    else:
        return a * expoDC(a*a, n/2)


# TEST
if __name__ == "__main__":
    print("4^3 with brute force = ",expoBF(4,3))
    print("4^3 with divide & conquer = ",expoDC(4,3))
