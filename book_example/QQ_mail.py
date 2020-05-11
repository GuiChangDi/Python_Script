#! python3
# 11.11.1 practice - use sys param to accept mail address and text content, use selenium log in email account,
# send to mail address.
# coding=utf-8

import sys
from selenium import webdriver
import time

mail_account = {
    'email_account':'changdig@foxmail.com',
    'password':'', #set password
}

log_in = 'https://mail.qq.com/'

send_mail = str(sys.argv[1])
send_text = str(sys.argv[2])

# Open qq mail page html
browser = webdriver.Chrome()
browser.get(log_in)
time.sleep(3)

# Input account and password
browser.switch_to.frame('login_frame')
browser.find_element_by_xpath('//*[@id="u"]').send_keys(mail_account['email_account'])
browser.find_element_by_xpath('//*[@id="p"]').send_keys(mail_account['password'])
browser.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(3)

# Write letter
browser.find_element_by_xpath('//*[@id="composebtn"]').click()
browser.switch_to.frame("mainFrame")
time.sleep(3)

# Add send mail
browser.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys(send_mail)
time.sleep(3)

# Add subject
browser.find_element_by_xpath('//*[@id="subject"]').send_keys('test python')
time.sleep(3)

# Add text
browser.switch_to.default_content()
browser.switch_to.frame('mainFrame')
browser.switch_to.frame(browser.find_element_by_class_name("qmEditorIfrmEditArea"))
browser.find_element_by_xpath('/html/body').send_keys(send_text)
time.sleep(3)

# send mail
browser.switch_to.parent_frame()
browser.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
