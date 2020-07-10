from selenium import webdriver
import time
import sys

from pynput.keyboard import Key, Controller
keyboard = Controller()






'''
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,

"proxyType":"MANUAL",
'''



driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen")
site = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")

for x in range(1, 5):

    play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
time.sleep(5)
play_btn.click()
time.sleep(5)
driver.refresh()
time.sleep(5)
keyboard.press(Key.space)
time.sleep(1)
keyboard.release(Key.space)
time.sleep(5)
driver.refresh()

