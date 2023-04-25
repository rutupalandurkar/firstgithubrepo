import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver=webdriver.Chrome("E:\chromedrivers\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="post-2669"]/div[2]/div/div/div[1]/p/iframe'))
src=driver.find_element(By.XPATH,'//*[@id="gallery"]/li[1]/img')
dst=driver.find_element(By.ID,'trash')
action.drag_and_drop(src,dst).perform()

# driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
# driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="post-2665"]/div[2]/div/div/div[1]/p/iframe'))
# src=driver.find_element(By.ID,'draggable')
# action=ActionChains(driver)
# action.drag_and_drop_by_offset(src,200,0).perform()





























