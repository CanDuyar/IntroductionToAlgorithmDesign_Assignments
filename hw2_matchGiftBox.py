# CAN DUYAR 171044075
# Question-5  / part c

def box_gift_pairs(boxes, gifts, l, h):
    if (l < h):
        pivo = divide_to_subarrays(boxes, l, h, gifts[h])
        divide_to_subarrays(gifts, l, h, boxes[pivo])
        updated_low = pivo + 1
        #divide the problems to subarray between updated_low and high for first patititon
        box_gift_pairs(boxes, gifts, updated_low, h)
        updated_high = pivo - 1
        #divide the problems to subarray between low and updated_high for second patititon
        box_gift_pairs(boxes, gifts, l,updated_high)


def divide_to_subarrays(box_or_gift, l, h, pivo):
    g = l
    t = l
    #when low and high is not conflict
    while t < h:
        if(box_or_gift[t] == pivo):
            box_or_gift[t], box_or_gift[h] = box_or_gift[h], box_or_gift[t]
            t -= 1
        elif(box_or_gift[t] < pivo):
            box_or_gift[g], box_or_gift[t] = box_or_gift[t], box_or_gift[g]
            g += 1

        t += 1
    box_or_gift[g], box_or_gift[h] = box_or_gift[h], box_or_gift[g]

    return g



# there are several boxes that have different sizes for boxes
boxes = [9,5,1,8,13,15]
#there are several gifts that have different sizes
gifts = [1,5,8,9,15,13]

box_gift_pairs(boxes, gifts, 0, len(boxes)-1)
#it prints mathes between boxes and gifts
for t in range(0,len(boxes)):
    print("gift that has {} size assigned to box that has {} size".format(gifts[t],boxes[t]))
