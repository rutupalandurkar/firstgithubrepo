from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("D:\\selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("https://automationtesting.in/")
driver.find_element(By.LINK_TEXT,"Demo Site").click()
SwitchTo = webdriver.find_element(By.PARTIAL_LINK_TEXT,"SwitchTo").click()
action=ActionChains(driver)
action.move_to_element(SwitchTo)
action.perform()

# action.click(driver.By.PARTIAL_LINK_TEXT,"Alerts")
driver.find_element(By.PARTIAL_LINK_TEXT,"Alerts").click()





















