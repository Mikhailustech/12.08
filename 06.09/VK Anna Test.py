# авторезация вк под  АННА ТЕСТ
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('C:/Users/mladygin/chromedriver.exe')
driver.get('https://vk.com/')
login = driver.find_element_by_xpath("//*[@id='index_email']")
login.send_keys('+79188995534')
password = driver.find_element_by_xpath("//*[@id='index_pass']")
password.send_keys('annadev1234')
enter = driver.find_element_by_xpath("//*[@id='index_login_button']")
enter.click()
time.sleep(4)
# Выход из учетки
#dropdown = driver.find_element_by_xpath("//*[@id='top_profile_link']")
#dropdown.click()
#exit = driver.find_element_by_xpath("//*[@id='top_logout_link']")
#exit.click()