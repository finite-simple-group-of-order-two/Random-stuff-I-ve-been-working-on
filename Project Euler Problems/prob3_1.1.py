from sympy.ntheory import factorint
def largestpf(num):
    largpf=0
    pflist=list(dict.keys(factorint(num)))
    for x in pflist:
        if x>=largpf:
            largpf=x
    return largpf

print("Largest prime factor of 600851475143 is : " +str(largestpf(600851475143)))