from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")


driver.get("https://demo.guru99.com/test/newtours/login.php")


user = driver.find_element(By.NAME, "userName")
user.click()
user.send_keys("")

ser = driver.find_element(By.XPATH,  "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input")
ser.click()
ser.send_keys("")

ln = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(5) > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > form > table > tbody > tr:nth-child(4) > td > input[type=submit]")
ln.click()

con = driver.find_element(By.PARTIAL_LINK_TEXT,  "SUPPORT").click()

ser = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/a/img")
ser.click()

inp = driver.find_element(By.LINK_TEXT, "Flights")
inp.click()

'''li = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
li.click()

lo = driver.find_element(By.LINK_TEXT, "Login")
lo.click()

ema = driver.find_element(By.ID, "email")
ema.click()
ema.send_keys("abc@gmail.com")

ps = driver.find_element(By.ID, "passwd")
ps.click()
ps.send_keys("abc123")

butn =  driver.find_element(By.TAG_NAME, "button")
butn.click()

driver.back()
driver.back()'''

radio = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[2]")
radio.click()

passenger = driver.find_element(By.NAME, "passCount")
passenger.click()
passenger.find_element(By.CSS_SELECTOR, "option[value='2']").click()

dep = driver.find_element(By.NAME, "fromPort")
dep.click()
dep.find_element(By.CSS_SELECTOR, "option[value='Paris']").click()

dm = driver.find_element(By.NAME, "fromMonth")
dm.click()
dm.find_element(By.CSS_SELECTOR, "option[value='2']").click()

dd = driver.find_element(By.NAME, "fromDay")
dd.click()
dd.find_element(By.CSS_SELECTOR, "option[value='19']").click()

des = driver.find_element(By.NAME, "toPort")
des.click()
des.find_element(By.CSS_SELECTOR, "option[value='London']").click()

rdm = driver.find_element(By.NAME, "toMonth")
rdm.click()
rdm.find_element(By.CSS_SELECTOR, "option[value='3']").click()

rdd = driver.find_element(By.NAME, "toDay")
rdd.click()
rdd.find_element(By.CSS_SELECTOR, "option[value='15']").click()

cl = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]").click()

air = driver.find_element(By.NAME, "airline")
air.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[10]/td[2]/select/option[2]").click()
air.send_keys(Keys.ENTER)

cont = driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[14]/td/input")
cont.click()











