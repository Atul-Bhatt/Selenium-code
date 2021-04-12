from selenium import webdriver  # webdriver performs all the UI actions.
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://medium.com")
