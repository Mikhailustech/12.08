# DEV1 авторезация под админкой на дев
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('C:/Users/mladygin/chromedriver.exe')
driver.get('https://dev1.im.usetech.ru/admin/')
login = driver.find_element_by_xpath("//*[@id='id_username']")
login.send_keys('admin@admin.ru')
password = driver.find_element_by_xpath("//*[@id='id_password']")
password.send_keys('Xswzaq123')