# Edu phyton_tests
from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/mladygin/chromedriver.exe')
driver.get('https://www.youtube.com/')
look = driver.find_element_by_xpath("//*[@id='search']")
look.send_keys('Fishing')
searh = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
searh.click()
time.sleep(5)
look.send_keys(' carp')
searh.click()
time. sleep(3)
driver.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dru%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fresults%253Fsearch_query%253DFishing&hl=ru&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#driver.find_element_by_xpath('//*[@id="button"]/yt-icon').click()
#driver.find_element_by_xpath('//*[@id="label"]/yt-formatted-string').click()
time.sleep(40)
driver.quit()