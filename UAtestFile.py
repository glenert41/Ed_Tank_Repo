from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

ua = UserAgent()
ua_chrome = str(ua.chrome)
opts = Options()

opts = Options()
#opts.add_argument("user-agent=[]")
# Below is tested line
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

driver = webdriver.Chrome(chrome_options=opts)

'''
driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver")
opts.add_argument(ua_chrome)
driver = webdriver.Chrome(chrome_options=opts)
'''

'''
profile = webdriver.Chrome()
profile.set_preference("general.useragent.override", ua_chrome)
driver = webdriver.Chrome(profile)
'''

'''
driver = webdriver.Chrome("/Users/owenmckenney/Downloads/chromedriver83")
options = webdriver.ChromeOptions()
options.add_argument("--user-agent=" + ua_chrome)
driver = webdriver.Chrome(options=options)
site = driver.get("google.com")
'''