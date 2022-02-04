from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome("C:\\Users\\Rajwinder\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe").get("https://demo.guru99.com/test/newtours/index.php")

'''i = d.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]')
i.click()'''

c = d.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a').click()

e = d.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[1]/td[2]/input').send_keys("abc")

f = d.find_element_by_xpath('/html/body').send_keys("abc")

g = d.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/input').click()