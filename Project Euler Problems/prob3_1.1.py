#Program to find largest prime factor of a given number

from sympy.ntheory import factorint
def largestpf(num):
    largpf=0
    pflist=list(dict.keys(factorint(num))) #read the sympy factorint() documentation for details, basically returns prime factors of a number as keys in a dicitonary
    for x in pflist:                       #basic loop to determine largest value in a list
        if x>=largpf:
            largpf=x
    return largpf

print("Largest prime factor of 600851475143 is : " +str(largestpf(600851475143)))