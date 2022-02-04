import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("C:\\Users\\Rajwinder\\PycharmProjects\\ Raj\\auto.htm.html")

city = driver.find_element(By.NAME,"city")
city.send_keys("high")
''''''
def txt(object):
    value = object.get_attribute('value')
    return len(value)


def test_city():
    assert 4 == txt(city)
    if 4 == txt(city):
        print("pass")
    else:
        print("fail")


'''
def obj(i):
  for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("")
    return len()

def test_city():
    assert 5 == len(obj(i))
blocks = int(input("Enter number of blocks: ")) 

for i in range(blocks + 1):
    for j in range(blocks + 1):
     height = j / 2
if height % 2 == 0:
    height = height / 2

print(f"The height of the pyramid: {height}")
def halfPyramid():
    for i in range(5):
        for j in range(i+1):
            print(end="* ")
        print()
def invertedHalfPyramid():
    for i in range(5):
        for j in range(i, 5):
            print(end="* ")
        print()
def fullPyramid():
    for i in range(5):
        for s in range(5, i+1, -1):
            print(end=" ")
        for j in range(i + 1):
            print(end="* ")
        print()
def invertedFullPyramid():
    for i in range(5):
        for s in range(i):
            print(end=" ")
        for j in range(i, 5):
            print(end="* ")
        print()
while True:
    print("1. Print Half Pyramid of Stars")
    print("2. Print Inverted Half Pyramid of Stars")
    print("3. Print Full Pyramid of Stars")
    print("4. Print Inverted Full Pyramid of Stars")
    print("5. Exit")
    print("Enter Your Choice: ", end="")
    choice = int(input())
    if choice==1:
        halfPyramid()
    elif choice==2:
        invertedHalfPyramid()
    elif choice==3:
        fullPyramid()
    elif choice==4:
        invertedFullPyramid()
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Wrong Choice!")
        
        def abc():
    a = 3
    b = 5
    c = a + b
    return c


expect_val = 8
actual_val = abc()

def test_a():
    assert expect_val == actual_val
'''''