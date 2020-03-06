#Name: Jayson Sandhu
#Student ID: 100659589
#Question 5

def zipMultiply(list1, list2,idx=0):
    if idx < min(len(list1), len(list2)):
        return [list1[idx] * list2[idx]] + zipMultiply(list1, list2, idx + 1)
    else:
        return []