#plix note that this does not work
from math import *
from functools import reduce
prod=1
def factors(num):
    faclist=[]
    for i in range (1, num):
        if num%i==0:
            faclist.append(i)
    return faclist

def factorz(n):    
    return list(reversed(list(set(reduce(list.__add__, 
                ([i, n//i] for i in reversed(list(range(1, int(n**0.5) + 1))) if n % i == 0))))))

def isprime(z):
    if z==2:
        return True
    else:
        return len(factorz(z))==2

def run():
    global prod
    i=1
    prod=1
    numlist=[]
    while i<=20:
        if set(factors(i)).issubset(set(numlist))==False:
            numlist=list(set(factors(i)).union(set(numlist)))
        elif floor(sqrt(i))-i==0.0:
            numlist.append(sqrt(i))
        elif isprime(i):
            numlist.append(i)
        i+=1
    
    for element in numlist:
        prod*=element
    print(prod)
    print(numlist)


run()


def test():
    global prod
    for z in range(1,20+1):
        print(bool((prod/z).is_integer))
