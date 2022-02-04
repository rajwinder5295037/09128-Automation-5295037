from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

name = driver.find_element(By.ID,"txtUsername")
name.send_keys("Admin")

pas = driver.find_element(By.NAME, "txtPassword")
pas.send_keys("admin123")

log = driver.find_element(By.CLASS_NAME, "button").click()

info = driver.find_element(By.XPATH,'//*[@id="menu_pim_viewMyDetails"]/b').click()

dash =driver.find_element(By.TAG_NAME,)
