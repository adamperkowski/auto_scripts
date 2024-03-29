 # https://coinpayu.com ads bot

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.binary_location = "/usr/lib/chromium/chromium"
options.add_argument(r"--user-data-dir=/home/adam/.config/chromium")
options.add_argument(r'--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)

driver.get("https://www.coinpayu.com/dashboard/ads_surf")

print(driver.title)

driver.implicitly_wait(10)

adlinks = driver.find_elements(by=By.XPATH, value="//div[@class='wrapper']")

print(adlinks)
