
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.douban.com")
driver.implicitly_wait(10)
#  1.前切换到子框架下，因为网页默不是登陆界面
driver.switch_to_frame(driver.find_elements_by_tag_name('iframe')[0])

#  2.先点击用账号密码登录的按钮
bottom1 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
bottom1.click()

driver.find_element_by_id("username").send_keys("18706937523")
driver.find_element_by_name("password").send_keys("041210liuyi")
time.sleep(3)
driver.find_element_by_class_name("account-form-field-submit").click()

driver.save_screenshot("douban01.png")
print("="*100)