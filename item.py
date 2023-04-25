from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWaitS
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
drget("http://127.0.0.1:8000//")
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('user')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('user')
driver.find_element(By.XPATH,'//*[@id="login-user"]/div/div/div[3]/div/button').click()
time.sleep(5)
# =============================add new====================================
driver.find_element(By.XPATH,'//ul[@class="navbar-nav me-auto mb-2 mb-lg-0"]//li[6]').click()
driver.find_element(By.XPATH,'//button[@id="add_new"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="itemname"]').send_keys('ed')
driver.find_element(By.XPATH,'//input[@name="itemdesc"]').send_keys('6')
driver.find_element(By.XPATH,'//input[@name="totalstock"]').send_keys('587')
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
# =================================edit========================================
time.sleep(5)
driver.find_element(By.XPATH,'//a[@data-id="1"][@title="Edit"]').click()
driver.find_element(By.XPATH,'//input[@id="totalstock"]').clear()
driver.find_element(By.XPATH,'//input[@id="totalstock"]').send_keys('465')
time.sleep(3)
driver.find_element(By.XPATH,'//button[@id="submit"]').click()
# =================================delete=========================================
time.sleep(5)
driver.find_element(By.XPATH,'//[@data-id="8"][@title="delete"]').click()
driver.find_element(By.XPATH,'//button[@id="confirm"]').click()
