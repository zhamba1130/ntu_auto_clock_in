#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
import os
from selenium import webdriver

username = 'Chanhsianghao'
password = 'Johnny135791130'

driver = webdriver.Chrome()
driver.get("https://my.ntu.edu.tw/mattend/ssi.aspx")

driver.find_element_by_xpath("//*[@class='btn btn-lg btn-info btn-block']").click()

driver.find_element_by_xpath("//*[@name='user']").send_keys(username)
driver.find_element_by_xpath("//*[@name='pass']").send_keys(password)
driver.find_element_by_xpath("//*[@name='Submit']").click()

time.sleep(2)

try:
    driver.find_element_by_xpath("//*[@id='btSign2']").click()
except:
    driver.find_element_by_xpath("//*[@id='btOtAgr']").click()
    driver.switch_to.alert.accept()
    driver.find_element_by_xpath("//*[@id='btSign2']").click()

driver.quit()
