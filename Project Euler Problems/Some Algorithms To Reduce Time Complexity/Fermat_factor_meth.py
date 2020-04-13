#basically a better trial and error method to factor an odd number, look up 
#Fermat's factorisation method for details I won't be explaining it here
from math import sqrt
x=1.0
y=1.0
faclist=[]
def factorman(num):
    if num%2!=0:
        for y in range(1,num):
            x=sqrt(num+y*y)
            if x.is_integer():
                faclist.append(x+y)
                faclist.append(x-y)
    return faclist

print(factorman(187))
