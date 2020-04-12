#functional but looks bad i'll fix it sometime idk

def munchausen(num):
    a=str(num)
    omega=0
    for x in a:
        z=pow(int(x), int(x))
        if(int(x)==0):
            z=0
        omega=omega+z
    if omega==int(num):
        return True
    else:
        return False
tau = 0
found =0
while(True):
    if munchausen(tau)==True:
        print(str(tau) + " is Munchausen")
        found=found+1
    tau+=1
    if found==4:
        print("I found 4 lol")
        break
        
