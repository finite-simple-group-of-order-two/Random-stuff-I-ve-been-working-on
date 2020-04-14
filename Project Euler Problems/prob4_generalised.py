#Program to find out the largest palindrome number that is a product of two, n-digit numbers
from math import sqrt
from math import ceil
from functools import reduce
import time

start=time.time()

#Function to generalise palindrome product finder to n digits
#let's say n is 3 here, the product of two 3-digit numbers can never exceed the product of the two
#largest 3 digit numbers ie 999*999, therefore we use 999*999 as our loop variable starting point and step the value down by 1
#after each iteration in the Main() function as we're interested in the largest one

digits=0                    #global variable to store number of digits
loopnum=0                   #global variable to store loop variable starting point
def largnumgen(zee):
    global digits
    global loopnum
    tong=''
    for loopnum2 in range(1, zee+1):
        tong+='9'
    loopnum=pow(int(tong),2)
    digits = zee

largnumgen(4) #replace 3 with n


#Boolean function to check if a number is palindrome
#basically works by converting input number 
#to string and reversing the string
def checkpalindrome(num):
    omega=str(num)
    revstring=''.join(reversed(omega))
    return revstring==omega

#function that returns all factors of input number as a list
def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

#function that takes in a list, which is usually the list of factors
#and returns a list with only those elements from input list that are n 
#digit numbers
def filter_3digit_factors(faclist):
    filtered_list=[]
    for i in faclist:
        if len(str(i))==digits:
            filtered_list.append(i)
    return filtered_list

#boolean function to check if a number is the product of two n-digit numbers
#basically, gets the factors of input number, filters out the n-digit factors and
#divides the n digit factors by the input number, one by one
#if the quotient is n-digit as well, means the number is a product of two 
#n-digit numbers
def triple_dig_prod(num):
    result = False
    for i in filter_3digit_factors(factors(num)):
        if len(str(ceil(num/i)))==digits:
            result=True
            break
    return result

#Calling all the functions to brute force the largest palindrome number that
#is a product of two n-digit numbers, in the Main() function
def Main():
    global loopnum
    while True:
        if checkpalindrome(loopnum)==True and triple_dig_prod(loopnum)==True:
            print("The largest palindrome number that is a product of two  "+str(digits)+"-digit numbers is "+str(loopnum))
            break
        loopnum-=1 #variable was declared before the triple_dig_prod() function 
Main()
print("Computation time : "+str(time.time()-start) + " seconds")

