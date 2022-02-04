from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://mail.google.com/mail/u/1/#inbox")

log = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
log.send_keys("studentexample@demo.studentnet.edu.au")
log.send_keys(Keys.ENTER)
 
user = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/input[1]")
user.send_keys("studentexample")

pas = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/input[2]")
pas.send_keys("demo1234")
pas.send_keys(Keys.ENTER)

time.sleep(5)
but = driver.find_element(By.LINK_TEXT, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
but.click()

sen = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div")
sen.click()





