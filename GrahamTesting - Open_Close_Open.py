from selenium import webdriver
import time
import keyboard



for x in range(1, 10):
    driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen")
    SoManyNights = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")
    low_play_btn = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]')

    time.sleep(2)
    low_play_btn.click()
    time.sleep(2)
    driver.close()
