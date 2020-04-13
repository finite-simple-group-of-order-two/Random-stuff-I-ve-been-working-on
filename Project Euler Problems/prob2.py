#finidng sum of even terms in fibonacci series that are less than or 4 million

def fibonacci_even_sum():
    i=1
    num=[1,1]                           #Manually defining first 2 elements of fibonacci series in a list
    sum=0
    while num[i]<=4000000:              #generating more members of series till they exceed 4 mil
        num.append(num[i]+num[i-1])     #adding newly generated elements into list
        if num[i]%2==0:                 #Checking for divisibility by 2
            sum=sum+num[i]
        i+=1
    return(sum)

print(fibonacci_even_sum())
