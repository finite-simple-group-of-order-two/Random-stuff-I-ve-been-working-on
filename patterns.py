#most of these should be easily generalised into n terms by change of a single variable

#pattern 1:
#1
#12
#123
#1234
#12345
def pattern1():
    i=1
    while i<=5:
        j=1
        while j<=i:
            print(j, end=' ')
            j+=1
        print("")
        i+=1

#pattern 2:
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14
def pattern2():
    i=1
    num=1
    while i<=5:
        j=1
        while j<=i:
            print(num, end=' ')
            j+=1
            num+=1
        print("")
        i+=1