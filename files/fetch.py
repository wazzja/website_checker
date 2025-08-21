import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import SELECTOR, SELECTOR_TYPE

bymap = {
        "TAG": By.TAG_NAME,
        "CLASS": By.CLASS_NAME,
        "CSS": By.CSS_SELECTOR
}

def fetch_url(url):
    options = Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        for attempt in range(3):
            try:
                print(f"[Attempt {attempt + 1}] Loading {url}")
                driver.get(url)
                break
            except Exception as e:
                print(f"[Attempt {attempt + 1}] driver.get() failed: {e}")
                time.sleep(2)
        else:
            print("[Error] Page failed to load after 3 attempts.")
            return []
        try:
            WebDriverWait(driver, 45).until(EC.presence_of_element_located((bymap[SELECTOR_TYPE], SELECTOR)))
            WebDriverWait(driver, 45).until_not(EC.presence_of_element_located((By.CLASS_NAME, "fa-spinner")))
            target = driver.find_elements(bymap[SELECTOR_TYPE], SELECTOR)
            return [i.get_attribute("innerHTML") for i in target]
        except:
            pass

    except TimeoutException:
        print(f"[Timeout] Failed to locate: {SELECTOR_TYPE}={SELECTOR}")
        return []

    finally:
        driver.quit()
