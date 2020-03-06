#Name: Jayson Sandhu
#Student ID: 100659589
#Question 2

def findMinAndMax(values):
    min_value = None
    for value in values:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value

    max_value = None 
    for value in values:
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value
        
    return (min_value, max_value)
