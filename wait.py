from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("E:\chromedrivers\chromedriver_win32 (5)\\chromedriver.exe")
# driver.implicitly_wait(10)
driver.get("https://automationtesting.in/")
driver.implicitly_wait(3)
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Demo Site").click()
SwitchTo = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"SwitchTo")))
driver.find_element(By.PARTIAL_LINK_TEXT,"SwitchTo").click()
action=ActionChains(driver)
action.move_to_element(SwitchTo)
action.perform()
action.click(driver.By.PARTIAL_LINK_TEXT,"Alerts")
driver.find_element(By.PARTIAL_LINK_TEXT,"Alerts").click()
