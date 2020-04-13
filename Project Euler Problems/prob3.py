#Finds the largest prime factor of a number
from math import sqrt

#Boolean Function to determine if a number is prime
def isprime(num):
    prime=True
    fac=0
    for i in range(1,num+1):
        if num%i==0:
            fac+=1
        if fac>2:
            prime=False
            break
    if num==1:
        prime=False
    return prime

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


#Function to cycle through all the factors of a number and check if they're prime
def largest_primefactor(zeta):
    large_pf=1
    for omega in factorman(zeta):
        if isprime(int(omega)):
            if omega>=large_pf:
                large_pf=omega
    return large_pf

print(largest_primefactor(600851475143))   
   