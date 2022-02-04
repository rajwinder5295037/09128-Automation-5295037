l1 = list() #empty list

x = input("How many elements do you want : ") #user tells the range(optional)

                          #iterating till user's range is reached
for i in range(int(x)):
    n = input()             #asking for input of 1 value
    l1.append(int(n))                     #adding that value to the list

print(l1)