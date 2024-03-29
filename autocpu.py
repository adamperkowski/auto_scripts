 # https://coinpayu.com ads bot

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.binary_location = "/usr/lib/chromium/chromium"
options.add_argument(r"--user-data-dir=/home/adam/.config/chromium")
options.add_argument(r'--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)

driver.get("https://www.coinpayu.com/dashboard/ads_surf")

driver.implicitly_wait(10)
blanklinks = driver.find_elements(by=By.XPATH, value="//div[@class='gray-all clearfix ags-list-box']")
adlinks = driver.find_elements(by=By.XPATH, value="//div[@class='text-overflow ags-description']")

for i in range(len(blanklinks), len(adlinks)):
# for i in range(len(adlinks)):
    adlinks[i].find_element(by=By.CSS_SELECTOR, value="span").click()
    sleep(int(adlinks[i].find_element(by=By.XPATH, value="../div[@class='ags-detail-point-time-report']").find_element(by=By.CLASS_NAME, value="ags-detail-time").text) + 15)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.close()
    driver.switch_to.window(tabs[0])


