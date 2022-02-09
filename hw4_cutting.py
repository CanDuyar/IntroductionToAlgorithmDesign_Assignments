# CAN DUYAR - 171044075 / solution of the minimum number of cuts problem based on decrease-and-conquer

def minimumNumberOfCuts(Nmeter,time = 0,control = 1):

    if (Nmeter <= 0):
        print("Minimum Number of Cuts for steel wire is: ",time)
        return time

    Nmeter = Nmeter-control
    control = control*2
    time = time + 1
    minimumNumberOfCuts(Nmeter,time,control)


if __name__ == "__main__":

    long=100;
    print("N = ",long)
    minimumNumberOfCuts(long)
