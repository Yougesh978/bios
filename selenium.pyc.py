from selenium import webdriver
PATH="C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
print(driver.title)
driver.quit()
