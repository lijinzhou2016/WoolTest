import time
import requests
from selenium import webdriver
import useragents
import wools
import xpaths
import proxys


wools = wools.get_all()

all_proxy = requests.get("http://www.qingool.com:8000/?protocol=1&country=%E5%9B%BD%E5%86%85").json()


for i in range(200):
    proxy = '--proxy-server=http://{}:{}'.format(all_proxy[i][0], all_proxy[i][1])
    xpath = xpaths.get()
    useragent = useragents.get()
    print(useragent)
    options = webdriver.ChromeOptions()
    options.add_argument(useragent)
    # options.add_argument(proxy)
    print(proxy)
    driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)

    for wool in wools:
        driver.get("http://www.baidu.com")
        time.sleep(3)
