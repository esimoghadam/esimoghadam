from operator import imod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import os

class bot:
    def __init__(self, username, password):
        self.username= username
        self.password= password
        self.driver = webdriver.Firefox()
    
    def login(self):
        driver= self.driver
        driver.get('https://instagram.com/')

        user = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div')
        user.send_keys(self.username)
        time.sleep(1)
        pas = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div')
        pas.send_keys(self.password)
        time.sleep(3)
        btn_log = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()