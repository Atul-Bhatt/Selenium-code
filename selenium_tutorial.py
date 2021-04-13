from selenium import webdriver  # webdriver performs all the UI actions.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

with open('data.txt', "r") as file:
    for line in file:
        driver.get("https://www.google.com/maps")
        search = driver.find_element_by_name("q")
        search.send_keys(line)
        search.send_keys(Keys.RETURN)

        try:
            span = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "section-star-display")))

            print(span.text)

        finally:
            driver.close()

# time.sleep(5)

# Quit a tab with driver.close() if you want to close entire browser(all the tabs)
# then use driver.quit()
# driver.close()
