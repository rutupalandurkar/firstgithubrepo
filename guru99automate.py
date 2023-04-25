from selenium import webdriver
from selenium.webdriver import ActionChains
# form selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("C:\Users\Dell\Downloads\chromedriver_win32 \chromedriver.exe")

driver.get("https://demo.guru99.com/v4/")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="uid"]').send_keys("mngr457122")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("mezAjyp")
driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()
driver.find_element(By.XPATH,'/html/body/div[3]/div/ul/li['2]/a').click()
time.sleep(3)
driver.find_element(By.XPATH,'//input[@name="name"]').send_keys("rutuja palandurkar")
driver.find_element(By.XPATH,'//input[@value="f"]').click()
driver.find_element(By.XPATH,'//input[@id="dob"]').send_keys("18-02-1998")
driver.find_element(By.XPATH,'//*[@name="addr"]').send_keys("wradhman nagar ambedkar squar nagpur")
driver.find_element(By.XPATH,'//*[@name="city"]').send_keys("nagpur")
driver.find_element(By.XPATH,'//*[@name="state"]').send_keys("maharashtra")
driver.find_element(By.XPATH,'//input[@name="pinno"]').send_keys("400002")
time.sleep(3)
driver.find_element(By.XPATH,'//input[@name="telephoneno"]').send_keys("9867948594")
driver.find_element(By.XPATH,'//input[@name="emailid"]').send_keys("abcjguy@gamail.com")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("ahoouja")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@value="Submit"]').click()
alert=Alert(driver).accept()

driver.find_element(By.PARTIAL_LINK_TEXT,"Edit Customer").click()
driver.find_element(By.XPATH,'//input[@name="cusid"]').send_keys("33284")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@name="AccSubmit"]').click()
alert=Alert(driver).dismiss()



