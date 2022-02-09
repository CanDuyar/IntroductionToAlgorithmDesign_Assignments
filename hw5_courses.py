# CAN DUYAR - 171044075 / a greedy algorithm that finds the maximum number of courses a student can attend among n courses.

def maxNumCourses(start,finish):
    courses = []
    t = 0
    courses.append(t)
    for g in range(len(finish)):
        if start[g] >= finish[t]:
            courses.append(g)
            t = g
    return len(courses)


#TEST
if __name__ == '__main__':
    start = [1 , 3 , 0 , 5 , 8 , 5]
    finish = [2 , 4 , 6 , 7 , 9 , 9]
    print("Maximum number of courses a student can attend among n courses is: ",maxNumCourses(start,finish))
