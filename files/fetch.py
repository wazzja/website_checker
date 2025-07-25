import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import SELECTOR, SELECTOR_TYPE

bymap = {
        "TAG": By.TAG_NAME,
        "CLASS": By.CLASS_NAME,
}

def fetch_url(url):
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.headless = True

    driver = uc.Chrome(options=options)

    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((bymap[SELECTOR_TYPE], SELECTOR)))
        WebDriverWait(driver, 30).until_not(EC.presence_of_element_located((By.CLASS_NAME, "fa-spinner")))
        if SELECTOR_TYPE == "CLASS":
            target = driver.find_elements(By.CSS_SELECTOR, f"div.content.{SELECTOR}")
        else:
            target = driver.find_elements(bymap[SELECTOR_TYPE], SELECTOR)
        return [i.get_attribute("innerHTML") for i in target]
    finally:
        driver.quit()
