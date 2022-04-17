# -*-coding:utf-8-*-

from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver=webdriver.Chrome(options=options)

# print(driver.capabilities['browserVersion'])
#
# print(driver.capabilities['browserName'])
# print(driver.capabilities['platformName'])
# print(driver.capabilities['timeouts'])