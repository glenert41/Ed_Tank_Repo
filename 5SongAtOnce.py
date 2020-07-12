import requests
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


def SoManyNights():
    SoManyNights = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")
    low_play_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_play_btn.click()
    time.sleep(6)
    low_pause_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_pause_btn.click()
    time.sleep(1)

def NewTab(url):

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    time.sleep(3)

def PlayandStop():
    high_play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
    high_play_btn.click()
    time.sleep(6)
    low_pause_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_pause_btn.click()
    time.sleep(1)

def CloseAllWindows():
    driver.quit()


for x in range (1,3):
    driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen")
    SoManyNights()

    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-ft-zay2x-fullclip')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-ft-jayv2')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-riptessa')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/free-madison-rnw-ed')
    PlayandStop()

    CloseAllWindows()

    time.sleep(2)
