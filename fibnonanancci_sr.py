

#fibonacci Series      : Done 27/3/21

def fab1(a,b):
    n = int(input("How many terms"))

    if n<=0:
        print("Please Enter Positive Interger or greater than 0")
    elif n==1:
        print("Fibonacci Series upto",n)

    else:   
        for i in range(int(n)):
            
            series = a*i**2+b
            print(series)


fab1(1,2)




