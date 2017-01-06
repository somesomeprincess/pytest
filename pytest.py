import time
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

#profile = FirefoxProfile(r'C:\Users\Yus\AppData\Roaming\Mozilla\Firefox\Profiles\esfmlmoa.default')

#driver = webdriver.Firefox(firefox_profile = profile , firefox_binary = binary)


driver=webdriver.Firefox()
print('1')
driver.get('http://yunpan.360.cn')
print('2')

driver.find_element_by_tag('quc-input-bg')
#driver.find_element_by_xpath(r'//*[@id="login"]/div/div[2]/form/p[1]/span/input').send_keys('maozzzzzzz@sina.com')
print('第一步')

time.sleep(3)
driver.find_element_by_xpath(r'//*[@id="login"]/div/div[2]/form/p[2]/span/input').send_keys('011720')
print('第二步')

time.sleep(3)
driver.find_element_by_xpath(r'//*[@id="login"]/div/div[2]/form/p[5]/input').click()
print('第三步')

time.sleep(3)
right_click = driver.find_element_by_xpath(r'//*[@id="list"]/li[50]/div[2]')
print('第四步')

time.sleep(3)
ActionChains(driver).context_click(right_click).perform()

