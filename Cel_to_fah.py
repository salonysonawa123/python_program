
print("if you want to converte celcius to fahrenhite Enter 1 and for vice-versa Press 2")

num = int(input("Enter value"))


if num==1:
    Celcuis = float(input("enter celcuis"))
    Fahrenheit = (Celcuis*1.8)+32
    print(Fahrenheit)

elif num==2:
    Fahrenheit = float(input("enter Fahrenheit"))
    Celcuis = (Fahrenheit-32)*(5/9)
    print(Celcuis)


