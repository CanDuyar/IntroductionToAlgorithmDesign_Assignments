
import sys
# CAN DUYAR - 171044075 / solution of the success rate of the first meaningful kth experiment problem based on decrease-and-conquer

def meaningfulExperiments(experiments, left, right, kth):
    if (kth > 0 and kth <= right - left + 1):
        loc = helperMeaningful(experiments, left, right)
        if (loc - left > kth - 1):
            return meaningfulExperiments(experiments, left, loc - 1, kth)
        if (loc - left == kth - 1):
            return experiments[loc]
        return meaningfulExperiments(experiments, loc + 1, right, kth - loc + left - 1)
    return sys.maxsize


def helperMeaningful(experiments, left, right):
    rightKeep = experiments[right]
    temp = left
    for t in range(left, right):
        if (experiments[t] <= rightKeep):
            experiments[temp], experiments[t] = experiments[t], experiments[temp]
            temp = temp + 1
    experiments[temp], experiments[right] = experiments[right], experiments[temp]
    return temp

#TEST
if __name__ == "__main__":

    experiments = [13, 9, 1, 4, 23, 11, 6]
    kth= 4;
    print("The success rate of the first meaningful kth experiment:", meaningfulExperiments(experiments, 0, len(experiments) - 1, kth))
