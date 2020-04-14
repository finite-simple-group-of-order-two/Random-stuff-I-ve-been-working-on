#Program to find out the largest palindrome number that is a product of two, 3-digit numbers
from math import sqrt
from math import ceil
from functools import reduce
import time

start=time.time()

#Boolean function to check if a number is palindrome
#basically works by converting input number 
#to string and reversing the string
def checkpalindrome(num):
    omega=str(num)
    revstring=''.join(reversed(omega))
    if revstring==omega:
        return True
    else:
        return False

#function that returns all factors of input number as a list
#ignore all the reversed() idk what I was trying
def factors(n):    
    return list(reversed(list(set(reduce(list.__add__, 
                ([i, n//i] for i in reversed(list(range(1, int(n**0.5) + 1))) if n % i == 0))))))

#function that takes in a list, which is usually the list of factors
#and returns a list with only those elements from input list that are 3 
#digit numbers
def filter_3digit_factors(faclist):
    filtered_list=[]
    for i in faclist:
        if len(str(i))==3:
            filtered_list.append(i)
    return filtered_list

#basically, the product of 2 3-digit numbers can never exceed the largest 6 digit number 
#so I used it as loop variable
loopnum=999999
res=0

#boolean function to check if a number is the product of two 3 digit numbers
#basically, gets the factors of input number, filters out the 3 digit factors and
#divides the 3 digit factors by the input number, one by one
#if the quotient is 3 digit as well, means the number is a product of two 
#3 digit numbers
def triple_dig_prod(num):
    result = False
    for i in filter_3digit_factors(factors(num)):
        if len(str(ceil(num/i)))==3:
            result=True
            break
    return result

#Calling all the functions to brute force the largest palindrome number that
#is a product of two 3-digit numbers
while True:
    if checkpalindrome(loopnum)==True and triple_dig_prod(loopnum)==True:
        print("The largest palindrome number that is a product of two  3-digit numbers is "+str(loopnum))
        break
    loopnum-=1 #variable was declared before the triple_dig_prod() function 

print("Computation time : "+str(time.time()-start) + " seconds")

