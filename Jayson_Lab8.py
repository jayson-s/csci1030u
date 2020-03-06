#Name: Jayson Sandhu
#Student ID: 100659589
#Description: A function that uses the insertion sort algorithim to sort a list

#Part 1
#Function Definition
def insertionSort(listIn):
    #Loop through the entire array starting at 1
    for x in range(1,len(listIn)):
        #Current value = list at position x
        currentValue = listIn[x]
        position = x

        #While the position is greater than 0 and the value in the list - 1
        # is greater than the current value continue modifying the list and
        # changing the position
        while position > 0 and listIn[position - 1] > currentValue:
            listIn[position] = listIn[position - 1]
            position = position - 1
        #Finally set the list at a position to the current value
        listIn[position] = currentValue
    #Finally print the list
    print(listIn)

#Test the function
insertionSort([4,3,7,1,8,2])
insertionSort([1000,12,3,12,44,341,243,33,4,566,7,8,2,34,343,123890343,6462498098,23,3890230932])
