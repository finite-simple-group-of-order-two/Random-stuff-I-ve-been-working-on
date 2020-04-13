#calculate sum of natural numbers less than or equal to 1000 that are divisible by 3 or 5
i=1
sum=0
while i<1000:
    if i%5==0 or i%3==0:
        sum=sum+i
    i+=1
print(sum) 