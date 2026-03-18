


def average(x=[]):
    answer=sum([i for i in x])/len(x)
    return answer

def median(x=[]):
    x.sort()
    answer=x[len(x)//2]
    return answer

def  standard_deviation(x=[]):
    std_lst=sum([(i-average(x))**2 for i in x])**0.5
    return std_lst
