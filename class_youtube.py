from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://www.youtube.com")

a = driver.find_element(By.XPATH, ' /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
a.click()
a.send_keys("hello")
a.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

print(driver.current_url)
print(driver.title)
al = len("https://www.youtube.com/results?search_query=hello")
expect_val1 = al

actual_val1 = len(driver.current_url)



def test_a():
    assert expect_val1 == actual_val1
    if(expect_val1 == actual_val1):
        print("yes it is hello")
    else:
        print("no it not hello")

b = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
b.click()

#------------------------------------------


driver.back()
#driver.back()


c = driver.find_element(By.XPATH, '   /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
c.click()
c.send_keys(Keys.CLEAR)
c.send_keys("neighbour")
c.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()
#d = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#d.click()


print(driver.current_url)
print(driver.title)
bl = len("https://www.youtube.com/results?search_query=neighbour")
expect_val2 = bl

actual_val2 = len(driver.current_url)

def test_b():
    assert expect_val2 == actual_val2
    if (expect_val2 == actual_val2):
        print("yes it is neighbour")
    else:
        print("no it not neighbour")
d = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
d.click()

#-----------------------------------------------

driver.back()

e = driver.find_element(By.XPATH, '     /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
e.send_keys(Keys.CLEAR)
e.click()
#e.send_keys(Keys.CLEAR)
e.send_keys("tesla")
e.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#f = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#f.click()
print(driver.current_url)
print(driver.title)
expect_val3 = len("https://www.youtube.com/results?search_query=tesla")

actual_val3 = len(driver.current_url)

def test_c():
    assert expect_val3 == actual_val3
    if (expect_val3 == actual_val3):
        print("yes it is tesla")
    else:
        print("no it not tesla")
f = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
f.click()

#------------------------------------------
driver.back()

g = driver.find_element(By.XPATH, '     /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
g.click()
g.send_keys(Keys.CLEAR)
g.send_keys("cryptocurrency")
g.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#h = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#h.click()
print(driver.current_url)
print(driver.title)
expect_val4 = len("https://www.youtube.com/results?search_query=cryptocurrency")

actual_val4 = len(driver.current_url)

def test_d():
    assert expect_val4 == actual_val4
    if (expect_val4 == actual_val4):
        print("yes it is cryptocurrenct")
    else:
        print("no it not cryptocurrency")
h = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
h.click()


#------------------------------------
driver.back()
i = driver.find_element(By.XPATH, '    /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
i.click()
i.send_keys(Keys.CLEAR)
i.send_keys("omnivox")
i.send_keys(Keys.ENTER)


#time.sleep(0.5)
#driver.back()

#j = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#j.click()
print(driver.current_url)
print(driver.title)
expect_val5 = len("https://www.youtube.com/results?search_query=omnivox")

actual_val5 = len(driver.current_url)

def test_e():
    assert expect_val5 == actual_val5
    if (expect_val5 == actual_val5):
        print("yes it is omnivox")
    else:
        print("no it not omnivox")
j = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
j.click()


#----------------------------------------
driver.back()

k = driver.find_element(By.XPATH, '      /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
k.click()
k.send_keys(Keys.CLEAR)
k.send_keys("whatsapp")
k.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#l = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#l.click()
print(driver.current_url)
print(driver.title)
expect_val6 = len("https://www.youtube.com/results?search_query=whatsapp")

actual_val6 = len(driver.current_url)

def test_f():
    assert expect_val6 == actual_val6
    if (expect_val6 == actual_val6):
        print("yes it is whatsapp")
    else:
        print("no it not whatsapp")
l = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
l.click()


#-----------------------------------------
driver.back()

m = driver.find_element(By.XPATH, '     /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
m.click()
m.send_keys(Keys.CLEAR)
m.send_keys("immigration")
m.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#n = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#n.click()
print(driver.current_url)
print(driver.title)
expect_val7 =len("https://www.youtube.com/results?search_query=immigration")

actual_val7 = len(driver.current_url)

def test_g():
    assert expect_val7 == actual_val7
    if (expect_val7 == actual_val7):
        print("yes it is immigration")
    else:
        print("no it not immigration")
n = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
n.click()


#---------------------------

driver.back()
o = driver.find_element(By.XPATH, '     /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
o.click()
o.send_keys(Keys.CLEAR)
o.send_keys("ircc")
o.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#p = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#p.click()
print(driver.current_url)
print(driver.title)
expect_val8 = len("https://www.youtube.com/results?search_query=ircc")

actual_val8 = len(driver.current_url)

def test_h():
    assert expect_val8 == actual_val8
    if (expect_val8 == actual_val8):
        print("yes it is ircc")
    else:
        print("no it not ircc")

p = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
p.click()

#---------------------------------
driver.back()

q = driver.find_element(By.XPATH, '      /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
q.click()
q.send_keys(Keys.CLEAR)
q.send_keys("quebec")
q.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()

#r = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#r.click()
print(driver.current_url)
print(driver.title)
expect_val9 = len("https://www.youtube.com/results?search_query=quebec")

actual_val9 = len(driver.current_url)

def test_i():
    assert expect_val9 == actual_val9
    if (expect_val9 == actual_val9):
        print("yes it is quebec")
    else:
        print("no it not quebec")
r = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[2]/ytd-button-renderer/a/yt-icon-button')
r.click()


#--------------

driver.back()
s = driver.find_element(By.XPATH, '   /html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
s.click()
s.send_keys(Keys.CLEAR)
s.send_keys("ontario")
s.send_keys(Keys.ENTER)

#time.sleep(0.5)
#driver.back()
#t = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
#t.click()
#/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[2]/input


print(driver.current_url)
print(driver.title)
expect_val10 = len("https://www.youtube.com/results?search_query=ontario")

actual_val10 = len(driver.current_url)

def test_j():
    assert expect_val10 == actual_val10
    if (expect_val10 == actual_val10):
        print("yes it is ontario")
    else:
        print("no it not ontario")

