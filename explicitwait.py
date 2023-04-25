import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("E:\chromedrivers\chromedriver_win32 (5)\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://demo.guru99.com/v4/")
exwt=WebDriverWait(driver,3)
# exwt. (ex).p (By.XPATH,'//input[@name="uid"]).
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="uid"]').send_keys("mngr457122")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("mezAjyp")
driver.find_element(By.XPATH,'//input[@name="btnLogin"]').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/ul/li['2]/a').click()
# time.sleep(3)
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