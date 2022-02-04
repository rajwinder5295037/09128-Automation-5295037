from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://s1.demo.opensourcecms.com/wordpress/contact-us/")

con = driver.find_element(By.PARTIAL_LINK_TEXT,  "Proudly powered by").click()


ln = driver.find_element(By.LINK_TEXT,  "Learn").click()

ser = driver.find_element(By.TAG_NAME,  "input")
ser.send_keys("testing")
ser.send_keys(Keys.ENTER)


the = driver.find_element(By.XPATH, "/html/body/div[2]/div/nav/ul/li[3]/a")
the.click()


scr = driver.find_element(By.CLASS_NAME, "drawer-toggle")
scr.click()

edu = driver.find_element(By.ID, "filter-id-education")
edu.click()

but =driver.find_element(By.CSS_SELECTOR,"#themes > div.wp-filter > div.filter-drawer > div.buttons > button.apply-filters.button.button-secondary")
but.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.back()



#name tag is incomplete
