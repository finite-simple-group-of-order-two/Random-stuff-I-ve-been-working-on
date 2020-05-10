def sumsquares(n):
    tau=0
    for i in range(1,n+1):
        tau+=(i*i)
    return tau

def squaresum(z):
    omega=0
    for i in range(1,z+1):
        omega+=i
    return omega*omega

print(abs(sumsquares(100)-squaresum(100)))
