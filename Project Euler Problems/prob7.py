from sympy import factorint
from math import ceil
from math import sqrt

def isprime(num):
    isp=True
    for i in range(2,ceil(sqrt(num))+1):
        if num%i==0:
            isp=False
            break
    if num==2:
        isp=True
    return isp

numlist=[]
i=2
while len(numlist)<10001:
    if isprime(i):
        numlist.append(i)
    i+=1

print(numlist[len(numlist)-1])





        