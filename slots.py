from random import random
from random import randint

#n-dimensional slot machine in python, with adjustable win probability. n>=3
#core idea being that the input is a number, and you generate as many random numbers as
#the input number, if all are equal, the player wins otherwise he loses. But the random number
#generator in py would almost never give 3 or more identical numbers in a row 
#so it is required to treat a difference of let's say 2 to be considered as equality

#function to generate a list of size num with each element being a 
#random number from 0 to 9
def slots(num): 
    a=list(range(0,num))
    for x in range(0, num):
        a[x]=randint(0,10)
    return a

#function to determine whether the player won or not, z is the size of slot machine
def winalg(z):

    win=True                                #boolean variable to store win/lose result

    omega=slots(z)                          #additonal list to store the output list of the slots() function cuz i like doing it that way

    i=1                                     #loop variable that ranges from 1 to (length of list)-1
    print(str(omega[0])+" ")
    while i<=(z-1):
        if abs(omega[i]-omega[i-1])<=2:     #defining a difference of two or less as equality, increasing the value on rhs of condition increases win rate so if u change 2 to 3 you'd be more likely to win

            omega[i]=omega[i-1]             #if our defined 'equality' is satisfied, we make sure the elements are conventionally equal
            print(str(omega[i])+" ")
        else:
            print(str(omega[i])+" ")
            win=False
        i+=1
    if win==True:
        print("\nomg u won pog")
    else:
        print("\no no u lost better luck next time")

winalg(4)                                   #calling the primary function, replace 3 with how big you'd like your slot machine
#this is a comment
