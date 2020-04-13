from math import sqrt
from math import ceil
from functools import reduce
def checkpalindrome(num):
    omega=str(num)
    revstring=''.join(reversed(omega))
    if revstring==omega:
        return True
    else:
        return False

def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def filter_3digit_factors(faclist):
    filter=