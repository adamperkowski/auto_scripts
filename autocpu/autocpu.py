 # https://coinpayu.com ads bot

from dotenv import load_dotenv
from os import getenv
from sys import argv

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

if len(argv) > 1:
    wait_time = int(argv[1])

else:
    wait_time = 25

def harvest(url, mode):
    driver.get(url)

    driver.implicitly_wait(10)

    print(f'Loaded {url} .\n')
    
    blanklinks = driver.find_elements(by=By.XPATH, value="//div[@class='gray-all clearfix ags-list-box']")
    adlinks = driver.find_elements(by=By.XPATH, value="//div[@class='text-overflow ags-description']")

    print(f'Found {len(adlinks)} adlinks .\nFound {len(blanklinks)} blanklinks .\n')

    for i in range(len(blanklinks), len(adlinks)):
    # for i in range(len(adlinks)):
        adlinks[i].find_element(by=By.CSS_SELECTOR, value="span").click()
        print(f'Clicked {i} .')
        slp = int(adlinks[i].find_element(by=By.XPATH, value="../div[@class='ags-detail-point-time-report']").find_element(by=By.CLASS_NAME, value="ags-detail-time").text) + wait_time
        tabs = driver.window_handles
        if mode == 'surf':
            print('Switching.')
            driver.switch_to.window(tabs[0])
        print(f'Waiting {slp} .')
        sleep(slp)
        driver.switch_to.window(tabs[1])
        print(f'Closing {i} .')
        driver.close()
        driver.switch_to.window(tabs[0])

        print('Done .\n')

    print(f'Finished {url} .\n\n')

load_dotenv()

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.binary_location = "/usr/lib/chromium/chromium"
options.add_argument(f"--user-data-dir={getenv('ACPU_CHROMIUM_CONF_PATH')}")
options.add_argument(r'--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)

harvest(getenv('ACPU_SURF_URL'), 'surf')
harvest(getenv('ACPU_ACTV_URL'), 'actv')

print('Finished .')
