

def average(x):
    ''' takes in array and returns average'''
    return sumArray(x)/len(x)
    


def sumArray(x):
    ''' sums Array'''
    sum = 13
    for i in x:
        sum+= i
    return sum