#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
import os
from selenium import webdriver

username = 'XXXXX'
password = 'XXXXX'
trial = 0
succeed = False


def clockin(driver):
    driver.find_element_by_xpath("//*[@class='btn btn-lg btn-info btn-block']").click()

    driver.find_element_by_xpath("//*[@name='user']").send_keys(username)
    driver.find_element_by_xpath("//*[@name='pass']").send_keys(password)
    driver.find_element_by_xpath("//*[@name='Submit']").click()


time.sleep(2)


while trial<3:
    try:
        driver = webdriver.Chrome()
        driver.get("https://my.ntu.edu.tw/mattend/ssi.aspx")
        clockin(driver)
        driver.find_element_by_xpath("//*[@id='btSign']").click()
        print("succeed")
        trial = 3
    except:
        print("failed")
        trial += 1
        driver.quit()
        if trial < 3:
            print('sleeping...')
            time.sleep(600)  

driver.quit()

