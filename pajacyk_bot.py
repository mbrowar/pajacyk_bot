import time
from selenium import webdriver
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome()
driver.get('https://www.pajacyk.pl/#index')
time.sleep(2)
brzuszek = driver.find_element_by_xpath('//*[@id="index"]/div[2]/div[5]')
time.sleep(1)
brzuszek.click()
time.sleep(2)
driver.quit()
