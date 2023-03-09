

def average(x):
    return sumArray(x)/len(x)
    


def sumArray(x):
    sum = 0
    for i in x:
        sum+= i
    return sum