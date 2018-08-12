from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(is_headless):
    chrome_options = Options()
    if is_headless:
        chrome_options.add_argument("--headless")
    chrome_options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'

    driver = webdriver.Chrome('./driver/chromedriver 3', chrome_options=chrome_options)
    return driver

driver = create_driver(False)
driver.get("http://www.google.com")
driver.find_element_by_id("lst-ib").send_keys("hi google")
driver.find_element_by_tag_name("button").click()