#function to print first n elements of fibonacci series
def nacci(n):
    num=list(range(1,n+1))              #defining array to store the fibonacci numbers
    num[0]=1
    num[1]=1
    tau=2
    while tau<n:                        #loop till all list items have been filled with fibonacci numbers
        num[tau]=num[tau-1]+num[tau-2]  #fibonacci number =  sum of previous two numbers in series
        tau+=1
    print(*num)
nacci(9)
