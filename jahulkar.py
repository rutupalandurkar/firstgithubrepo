from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome(  )
#------- E:\chromedrivers\chromedriver_win32 (5)\\chromedriver.exe")--------
driver.get("http://127.0.0.1:8000//")
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('user')
# driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys('PALANDURKAR')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('user')
driver.find_element(By.XPATH,'//*[@id="login-user"]/div/div/div[3]/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//ul[@class="navbar-nav me-auto mb-2 mb-lg-0"]//li[4]').click()
driver.find_element(By.XPATH,'//*[@class="btn btn-primary rounded-0 bg-gradient btn-sm"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="helpername"]').send_keys("Abhir")
driver.find_element(By.XPATH,'//input[@name="phoneno"]').send_keys('9867985960')
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
time.sleep(5)
# driver.find_element(By,'//input[@type="search"]').click()

driver.find_element(By.XPATH,'//*[@id="helper-list"]/tbody/tr[6]/td[4]/a').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
driver.find_element(By.XPATH,'//*[@id="helper-list"]/tbody/tr[7]/td[5]/a').click()
driver.find_element(By.XPATH,'//*[@id="confirm"]').click()