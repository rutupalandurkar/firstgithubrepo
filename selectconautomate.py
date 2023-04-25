from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("D:\\selenium\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://automationtesting.in/")
driver.find_element(By.LINK_TEXT,"Demo Site").click()
selectcountry=Select(driver.find_element(By.ID,"countery"))
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span').click()
driver.find_element(By.XPATH,"/html/body/span/sapn/span[1]/input").send_keys("india")
driver.find_element(By.XPATH,'//*[@id="select2-country-results"]/li[1]').click()
selectcountry.select_by_visible_text("india")
