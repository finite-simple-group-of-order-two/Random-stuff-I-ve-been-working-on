#finidng sum of even terms in fibonacci series

def fibonacci_even_sum():
    i=1
    num=[1,1]
    sum=0
    while num[i]<=4000000:
        num.append(num[i]+num[i-1])
        if num[i]%2==0:
            sum=sum+num[i]
        i+=1
    return(sum)

print(fibonacci_even_sum())
