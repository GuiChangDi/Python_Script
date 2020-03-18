from selenium import webdriver

driver = webdriver.Chrome()

#access baidu
first_url = 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

#acess news page
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

#return to baidu
print("back to %s" %(first_url))
driver.back()

#move to news page
print("move to  %s" %(second_url))
driver.forward()

driver.quit()