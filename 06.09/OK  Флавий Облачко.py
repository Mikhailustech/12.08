# авторизация вк под Флавий облачкои и получение токена для подключения к группе
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('C:/Users/mladygin/chromedriver.exe')
driver.get('https://ok.ru/dk?st.cmd=anonymMain&st.layer.cmd=PopLayerClose')
login = driver.find_element_by_xpath("//*[@id='field_email']")
login.send_keys('79286115257')
password = driver.find_element_by_xpath("//*[@id='field_password']")
password.send_keys('usetechtest123')
enter = driver.find_element_by_xpath("//*[@id='anonymPageContent']/div[2]/div/div[3]/form/div[5]/div[1]/input")
enter.click()
time.sleep(2)
driver.get('https://ok.ru/group/57695928647891/settings/messages')
access_key = driver.find_element_by_xpath("//*[@id='group-settings-form']/div[1]/div[2]/div/div[5]/div/a")
access_key.click()
#Update key
get_new_access_key = driver.find_element_by_xpath('//*[@id="hook_FormButton_button_change_token"]')
get_new_access_key.click()
time.sleep(2)
new_key = driver.find_element_by_xpath("//*[@id='hook_Form_PopLayerAltGroupChangeTokenForm']/form/input[3]")
key = new_key.get_attribute("value")

# Проверяем на корректность если слово 'time' есть, значит ключ выводим на печать.
driver.get("https://api.ok.ru/graph/me/subscriptions?access_token="+str(key))
#time.sleep(2)
#assert "Invalid" in driver.page_source
#print("log")
time.sleep(2)
assert "time" in driver.page_source
print(key)
driver.__exit__()

# https://ok.ru/group/57695928647891/messages ссылка на диалог с группой флавием облочко