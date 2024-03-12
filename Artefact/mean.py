def mean(list):
    sum = 0 
    for i in list:
        sum = i+sum
    average = sum / len(list)
    return average