m1 = input("Enter number 1:")
m2 = input("Enter number 2:")

sum = float(m1) + float(m2)
sub = float(m1) - float(m2)
mu = float(m1) * float(m2)
div = float(m1) / float(m2)
sub2 = float(m2) - float(m1)
div2 = float(m2) / float(m1)

if(m1>m2):
    print("subtraction is :",sub)
else:
    print("subtraction is :", sub2)

print("sum is :",sum)

print("multiplication is :",mu)

if(m1>m2):
    print("division is :",div)
else:
    print("division is :", div2)

stu1 = input("Enter student first name :")
stu2 = input("Enter student last name :")

m1 = input("Enter marks of OOP:")
m2 = input("Enter marks of Database1:")
m3 = input("Enter marks of Dtabase2:")
sum1 = stu1 + " " + stu2
print("Student name is : ",sum1)

sum2 = float(m1) + float(m2) + float(m3)
print("Student total marks is: ",sum2)

av = sum2 / 3
print("The average of marks is : " ,av)

//
print("hello")#first code

num1=22.7#second code
num2=3.14
sum=num1+num2
print("sum is:",sum)

Num1=input('enter number 1')#third code
Num2=input('enter number 2')
Sum=float(Num1)+float(Num2)
print("sum is:",Sum)

#last code
num1=input('enter number 1')
num2=input('enter number 2')
sum=(num1)+(num2)
print("sum of {0} ad {1} is {2}" .format(num1, num2, sum))
print("sum is:",sum)
