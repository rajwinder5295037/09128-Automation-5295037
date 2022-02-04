from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
#from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://www.google.com")

def qw():
    a = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    a = driver.click()
    a.send_keys("hello")
    a.send_keys(Keys.ENTER)
    b = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]')
    b = driver.click()

    print(driver.current_url)
    print(driver.title)
    expect_val1 = "hello - Google Search"
    actual_val1 = driver.title

    def test_a():
        assert expect_val1 == actual_val1

qw()


def aw():
    a = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()
    a.send_keys("hell")
    a.send_keys(Keys.ENTER)
    b = driver.find_element(By.XPATH,
                            '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[1]').click()

    print(driver.current_url)
    print(driver.title)
    expect_val2 = "hell - Google Search"
    actual_val2 = driver.title

    def test_b():
        assert expect_val2 == actual_val2

aw()



'''que = driver.find_element(By.XPATH, "//input[@name='q']")
que.send_keys("Software")
time.sleep(2)
#que.send_keys(Keys.ARROW_DOWN)
#que.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
que.send_keys(Keys.RETURN)'''

