#calculates factorial of a number num
def factorial(num):
    fac=1
    for x in range(1,num+1):
        fac=fac*x
    return fac

#calculates number or ways to choose r things out of n distinct things ie ncr
def choose(num1, num2):
    res=(factorial(num1))/(factorial(num1-num2)*factorial(num2))
    return res

#calculates number of ways to arrange n things taken r at a time, ie npr
def permutate(num1, num2):
    res=choose(num1, num2)*factorial(num2)
    return res

#calculates sum of first n elements of an arithmetic progression with first element 'a', and common difference 'd'
def sumap(a, d, n):
    res=(n/2)*(2*a + d*(n-1))
    return res

#calculates sum of squares of first n natural numbers
def sumsquarenatural(num):
    res=n*(n+1)*(2*n + 1)/6
    return res

#calculates sum of cubes of first n natural numbers
def sumcubenatural(num):
    res=sumap(1,1, n)*sumap(1,1, n)
    return res

#calculates sum of first n terms of a gp with first term 'a' and common difference 'r'
def sumgp(a,r,n):
    res=0
    if r>1:
        res=a*(pow(r,n)-1)/(n-1)
    elif r<1:
        res=a*(1-pow(r,n))/(1-r)
    return res