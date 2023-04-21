import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "/Users/harshsaxena/Drivers/chromedriver")
driver.implicitly_wait(6)
parent_handle =driver.get("https://bestexresearch.com/")
driver.maximize_window()
wait = WebDriverWait (driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='nav-menu-item-11213']/a/span/span[1]/span[2]")))
Algorithm = driver.find_element(By.XPATH,"//*[@id='nav-menu-item-11213']/a/span/span[1]/span[2]")
Equities= driver.find_element(By.XPATH,"//*[@id='nav-menu-item-11189']/a/span/span[1]/span[2]")
Futures= driver.find_element(By.XPATH,"//*[@id='nav-menu-item-11196']/a/span/span[1]/span[2]")
FX =driver.find_element(By.XPATH,"//*[@id='nav-menu-item-11192']/a/span/span[1]/span[2]")
actions = ActionChains(driver)
time.sleep(4)
actions.move_to_element(Algorithm).move_to_element(Equities).perform()
time.sleep(6)
parent_handle = driver.current_window_handle

#FX page
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/a[1]/span").click()
time.sleep(6)
driver.switch_to.window(parent_handle)# switched to homepage
time.sleep(6)

#futures page
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/a[2]/span")
time.sleep(6)

driver.switch_to.window(parent_handle)# switched to homepage
time.sleep(6)

#equities page
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/a[3]/span").click()
time.sleep(4)
driver.switch_to.window(parent_handle)
time.sleep(6)


# open youtube link to play video
driver.switch_to.new_window()
driver.get("https://youtu.be/tg9fY3zA2r4")
time.sleep(30)
driver.close()
time.sleep(4)
driver.switch_to.window(parent_handle)
#close all windows
driver.quit()
