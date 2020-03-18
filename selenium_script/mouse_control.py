from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#locate the elem
above = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(above).perform()
print("进入设置")

driver.quit()