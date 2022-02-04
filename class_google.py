from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://www.google.com")

a = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
a.click()
a.send_keys("hello")
a.send_keys(Keys.ENTER)

#b = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#b.click()

#time.sleep(0.5)
#driver.back()

print(driver.current_url)
print(driver.title)
expect_val1 = "hello - Google Search"

actual_val1 = driver.title

def test_a():
    assert expect_val1 == actual_val1
    if(expect_val1 == actual_val1):
        print("yes it is hello")
    else:
        print("no it not hello")



#------------------------------------------

driver.back()
c = driver.find_element(By.XPATH, ' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
c.click()
c.send_keys("neighbour")
c.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()
#d = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#d.click()


print(driver.current_url)
print(driver.title)
expect_val2 = "neighbour - Google Search"

actual_val2 = driver.title

def test_b():
    assert expect_val2 == actual_val2
    if (expect_val2 == actual_val2):
        print("yes it is neighbour")
    else:
        print("no it not neighbour")


#-----------------------------------------------

driver.back()
e = driver.find_element(By.XPATH, ' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
e.click()
e.send_keys("tesla")
e.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#f = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#f.click()
print(driver.current_url)
print(driver.title)
expect_val3 = "tesla - Google Search"

actual_val3 = driver.title

def test_c():
    assert expect_val3 == actual_val3
    if (expect_val3 == actual_val3):
        print("yes it is tesla")
    else:
        print("no it not tesla")


#------------------------------------------
driver.back()

g = driver.find_element(By.XPATH, ' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
g.click()
g.send_keys("cryptocurrency")
g.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#h = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#h.click()
print(driver.current_url)
print(driver.title)
expect_val4 = "cryptocurrency - Google Search"

actual_val4 = driver.title

def test_d():
    assert expect_val4 == actual_val4
    if (expect_val4 == actual_val4):
        print("yes it is cryptocurrenct")
    else:
        print("no it not cryptocurrency")


#------------------------------------
driver.back()
i = driver.find_element(By.XPATH, ' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
i.click()
i.send_keys("omnivox")
i.send_keys(Keys.ENTER)


#time.sleep(0.5)
#driver.back()

#j = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#j.click()
print(driver.current_url)
print(driver.title)
expect_val5 = "omnivox - Google Search"

actual_val5 = driver.title

def test_e():
    assert expect_val5 == actual_val5
    if (expect_val5 == actual_val5):
        print("yes it is omnivox")
    else:
        print("no it not omnivox")


#----------------------------------------
driver.back()

k = driver.find_element(By.XPATH, ' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
k.click()
k.send_keys("whatsapp")
k.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#l = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#l.click()
print(driver.current_url)
print(driver.title)
expect_val6 = "whatsapp - Google Search"

actual_val6 = driver.title

def test_f():
    assert expect_val6 == actual_val6
    if (expect_val6 == actual_val6):
        print("yes it is whatsapp")
    else:
        print("no it not whatsapp")


#-----------------------------------------
driver.back()

m = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
m.click()
m.send_keys("immigration")
m.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#n = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#n.click()
print(driver.current_url)
print(driver.title)
expect_val7 = "immigration - Google Search"

actual_val7 = driver.title

def test_g():
    assert expect_val7 == actual_val7
    if (expect_val7 == actual_val7):
        print("yes it is immigration")
    else:
        print("no it not immigration")


#---------------------------

driver.back()
o = driver.find_element(By.XPATH, ' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
o.click()
o.send_keys("ircc")
o.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#p = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#p.click()
print(driver.current_url)
print(driver.title)
expect_val8 = "ircc - Google Search"

actual_val8 = driver.title

def test_h():
    assert expect_val8 == actual_val8
    if (expect_val8 == actual_val8):
        print("yes it is ircc")
    else:
        print("no it not ircc")


#---------------------------------
driver.back()

q = driver.find_element(By.XPATH, ' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
q.click()
q.send_keys("quebec")
q.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#r = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#r.click()
print(driver.current_url)
print(driver.title)
expect_val9 = "quebec - Google Search"

actual_val9 = driver.title

def test_i():
    assert expect_val9 == actual_val9
    if (expect_val9 == actual_val9):
        print("yes it is quebec")
    else:
        print("no it not quebec")


#--------------

driver.back()
s = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input ')
s.click()
s.send_keys("ontario")
s.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()
#t = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#t.click()
#/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[2]/input


print(driver.current_url)
print(driver.title)
expect_val10 = "ontario - Google Search"

actual_val10 = driver.title

def test_j():
    assert expect_val10 == actual_val10
    if (expect_val10 == actual_val10):
        print("yes it is ontario")
    else:
        print("no it not ontario")



