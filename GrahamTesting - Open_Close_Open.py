from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/grahamlenert/Downloads/chromedriverowen")
counter = 0

for x in range(1, 5):

    SoManyNights = driver.get("https://soundcloud.com/eddison-duolo-546732382/so-many-nights-ed-tank")

    play_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')

    time.sleep(5)
    play_btn.click()
    time.sleep(5)
    driver.close()
    time.sleep(1)
    counter = counter + 1
    print(counter)