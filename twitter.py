from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://twitter.com/login")
time.sleep(3)
search_username = driver.find_element_by_xpath("/html/body")
search_username.send_keys('@kokusyenet')
search_password = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
time.sleep(1)
search_password.send_keys('ryoga1023')
search_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button")
search_login.submit()
time.sleep(10)
search_coment = driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')
time.sleep(2)
search_coment.send_keys("seleniumから送信成功！！やったー！")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div[2]/button").click()
time.sleep(3)
#driver.quit()
