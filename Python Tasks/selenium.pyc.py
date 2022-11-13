from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH="C:\Program Files (x86)\chromedriver.exe"
#filepath ="C:\Users\USER\OneDrive\Desktop\Pentest\shellscript.txt"
driver = webdriver.Chrome(PATH)

driver.get("http://the-internet.herokuapp.com/upload")
print(driver.title)

search = driver.find_element(By.ID, "file-upload")
#search.clear()
search.send_keys(r"C:\Users\USER\OneDrive\Desktop\Pentest\logo.png")   #this for the upload 
#search.send_keys("getting started with python")
#search.send_keys(Keys.RETURN)
#search.send_keys(Keys.RETURN)
# print(driver.page_source) to get the source code as an output
upload=driver.find_element(By.ID, "file-submit")       #for submit button
upload.click()

result=driver.find_element(By.TAG_NAME, "h3")
print(result.text)

time.sleep(15)

driver.quit()
