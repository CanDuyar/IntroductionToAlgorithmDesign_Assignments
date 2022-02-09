# CAN DUYAR - 171044075 / Question 3

def count_substr_brute_force(str,start,end) :

    count = 0
    for t in range(0, len(str)):
        if (str[t] == start):
            for g in range(t+1, len(str)):
                if (str[g] == end):
                    count = count + 1

    return count # number of substrings


#TEST
if __name__ == "__main__":

    example = "TXZXXJZWX";
    start = "X"
    end = "Z"
    print("Number of substrings =",count_substr_brute_force(example,start,end))
