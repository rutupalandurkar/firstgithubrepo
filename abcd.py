import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("D:\\selenium\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://automationtesting.in/")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()
action=ActionChains(driver)
switchto=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"SwitchTo")))
action.move_to_element(switchto).perform()
windlink=driver.find_element(By.PARTIAL_LINK_TEXT,"Windows")
action.click_and_hold(on_element=windlink).perform()
time.sleep(10)

action.release(on_element=windlink).perform()