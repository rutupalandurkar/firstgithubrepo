import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("E:\chromedrivers\chromedriver_win32 (5)\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://mitintech.com/")
driver.find_element(By.PARTIAL_LINK_TEXT,'Wedriver.maximize_window()
b Support').click()
driver.find_element(By.XPATH,'/html/body/nav/ul/li[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="mymodal"]/div/div/div[2]/form/div/input[1]').send_keys('rutu')
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div/input[2]').send_keys('rutu')
driver.find_element(By.XPATH,'//*[@id="mymodal"]/div/div/div[2]/form/div/input[4]').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Edit Account').click()
driver.find_element(By.XPATH,'//input[@id="id_first_name"]').send_keys()
driver.find_element(By.XPATH,'//input[@name="last_name"]').send_keys('raut')
driver.find_element(By.XPATH,'//input[@value="palandurkarrutu@gamil.com"]').send_keys()
driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[4]/td/input').send_keys('rutu@123')
driver.find_element(By.XPATH,'/html/body/div/table/tbody/tr[5]/td/input').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'Change Password').click()
# driver.find_element(By.XPATH,'/html/body/div/form/input[2]').send_keys('rutu')
# driver.find_element(By.XPATH,'/html/body/div/form/input[3]').send_keys('rutu')