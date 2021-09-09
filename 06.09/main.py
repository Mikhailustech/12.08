# DEV1 авторезация под Фалииева Анна
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('C:/Users/mladygin/chromedriver.exe')
driver.get('http://mlgext.usetech.ru')
login = driver.find_element_by_xpath("/html/body/app/div/div/div/login-form/div/div/div/form/div[1]/input")
login.send_keys('mg10.f2017@yandex.ru')
password = driver.find_element_by_xpath ("/html/body/app/div/div/div/login-form/div/div/div/form/div[2]/input")
password.send_keys('intel444')
# для Бетта
#driver = webdriver.Chrome('C:/Users/mladygin/chromedriver.exe')
#driver.get('https://beta-im.mlg.ru/')
#login = driver.find_element_by_xpath("/html/body/app/div/div/div/login-form/div/div/div/form/div[1]/input")
#login.send_keys('test2@beta.ru')
#password = driver.find_element_by_xpath ("/html/body/app/div/div/div/login-form/div/div/div/form/div[2]/input")
#password.send_keys('user2beta2234')
enter = driver.find_element_by_xpath("/html/body/app/div/div/div/login-form/div/div/div/form/button")
enter.click()
time.sleep(8)
Graphics = driver.find_element_by_xpath ("/html/body/app/div/div/sidebar/div/ul/li[3]/a")
Graphics.click()
time.sleep(6)
Special_graphics = driver.find_element_by_xpath ("/html/body/app/div/div/div/reports/reports-analysis-demo/div/filters-panel/div/div/div[2]/sub-menu/div/ul/li[5]/a/span")
Special_graphics.click()
time.sleep(3)
Search = driver.find_element_by_xpath("/html/body/app/div/div/div/reports/reports-special/div/div/div[2]/div[1]/references-dropdown/p-dropdown/div/div[3]/span")
Search.click()

sel = Select(driver.find_element_by_tag_name("OBL_reg_reportHandler"))
sel.select_by_selector("body > div > div.ui-dropdown-items-wrapper > ul > li:nth-child(45) > div")

# Search2 = driver.find_element_by_xpath("/html/body/div/div[1]/input")
# Search2.send_keys('OBL_reg_reportHandler')
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/div/div[2]/ul/li/div/span").click
# time.sleep(1)
# Create = driver.find_element_by_xpath("/html/body/app/div/div/div/reports/reports-special/div/div/div[2]/div[2]/button")
# Create.click()
