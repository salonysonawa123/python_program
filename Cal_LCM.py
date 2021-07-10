
###Python program to find the L.C.M. of two input number

##Method 1
# def compute_gcd(x, y):

#    while(y):
#        x, y = y, x % y
#        print(x,"and",y)
#    return x

# # This function computes LCM
# def compute_lcm(x, y):
#    lcm = (x*y)//compute_gcd(x,y)
#    return lcm

# num1 = 52
# num2 = 24

# print("The L.C.M. is", compute_lcm(num1, num2))


##method 2

def compute_gcd(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
    

def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x,y)
    return lcm

num1 = 14
num2 = 16

print("The L.C.M. is", compute_lcm(num1, num2))


