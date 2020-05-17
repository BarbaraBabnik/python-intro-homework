a=int(input("Enter a value for a: "))

b=int(input("Enter a value for b: "))

math=input("Which arithmetic operation do you want? Choose + , -, / or *: ")

if math == "+":
    print(a + b)

elif math == "-":
    print(a - b)

elif math == "*":
    print(a * b)

elif math == "/":
    print(a / b)

else:
    print("Something went wrong ...")