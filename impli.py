from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://s1.demo.opensourcecms.com/wordpress/")

login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")

name = driver.find_element_by_id("txtPassword")
name.send_keys("admin123")

log = driver.find_element_by_id("btnLogin").click()

info = driver.find_element_by_xpath('//*[@id="menu_pim_viewMyDetails"]/b').click()

info.forward()