from selenium import webdriver
import time
# from ProxyLibrary import *
from random_proxies import random_proxy

print(random_proxy(use_cache=False))

'''
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,

    "proxyType": "MANUAL",

}

driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver")
site = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")

for x in range(1, 5):

    play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
    time.sleep(1)
    play_btn.click()
    time.sleep(5)
    driver.refresh()
    time.sleep(1)


# /Users/owenmckenney/Desktop/SoundcloudBot/venv/bin/python

'''