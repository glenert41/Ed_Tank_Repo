import requests
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

SongDuration = 3


def SoManyNights():
    driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")
    high_play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
    high_play_btn.click()
    time.sleep(SongDuration)
    low_pause_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_pause_btn.click()
    time.sleep(1)

def NewTab(url):

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    time.sleep(1)

def PlayandStop():
    high_play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
    high_play_btn.click()
    time.sleep(SongDuration)
    low_pause_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')
    low_pause_btn.click()


def CloseAllWindows():
    driver.quit()

<<<<<<< HEAD:5SongAtOnce.py
for x in range (1,3):
    driver = webdriver.Chrome("/Users/owenmckeney/Downloads/chromedriver")
=======

for x in range (1,120):

    #Option to run headless
    #driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen", options=chrome_options)

    #Option to run with head
    driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen")

>>>>>>> origin/master:MultiSongStreaming.py
    SoManyNights()

    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-ft-zay2x-fullclip')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-ft-jayv2')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/lil-pacco-riptessa')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/free-madison-rnw-ed')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/rnw-ed-next-up')
    PlayandStop()
    NewTab('https://soundcloud.com/eddison-duolo-546732382/ed-mama-is-proud-of-me')
    PlayandStop()

    CloseAllWindows()

    time.sleep(1)
