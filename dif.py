num1 = input("enter n1")
num2 = input("enter n2")
num3 = input("enter n3")
sum = int(num1) + int(num2) + int(num3)
if num1 < num2:
    print("This is greater number:", num2)
elif num1 < num3:
    print("This is greater number:", num3)
else:
    print("This is greater number:", num1)
