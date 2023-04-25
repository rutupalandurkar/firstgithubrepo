from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome("E:\chromedrivers\chromedriver_win32 (5)\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:8000//")
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('user')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('user')
driver.find_element(By.XPATH,'//*[@id="login-user"]/div/div/div[3]/div/button').click()
