# coding: utf-8 
from selenium import webdriver
import time

# 实例化webdriver
driver =webdriver.Chrome()

driver.find_element_by_id('form_email').send_keys('')
driver.find_element_by_id('from_password').send_keys('')

time.sleep()