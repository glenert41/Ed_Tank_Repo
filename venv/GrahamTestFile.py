import requests
import random
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen", options=opts)



def SoManyNights():
    SoManyNights = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")
    low_play_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_play_btn.click()
    time.sleep(30)
    driver.close()