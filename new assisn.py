
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.bestbuy.ca/en-ca?intlreferer=&intlredir=https://www.bestbuy.com/")


cdnFlag = driver.find_element(By.CLASS_NAME, "flyoutNavigationGroup_3HN52")
cdnFlag.click()

actnChns = ActionChains(driver)
actnChns.move_to_element(cdnFlag)
actnChns.click_and_hold(cdnFlag)

time.sleep(10)

'''phone = driver.find_element(By.CLASS_NAME, "offerBackgroundImage_1Y4GG xsTwoAcrossImage_s5wkR skuImage_176Ck")
phone.click()
actnChn = ActionChains(driver)
actnChn.move_to_element(phone)
actnChn.click_and_hold(phone)'''
