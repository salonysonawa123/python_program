
num = int(input("Enter Number"))
sum =0
for i in range(len(str(num))):
    sum = num%10 + sum
    num = int(num/10)

print(sum)