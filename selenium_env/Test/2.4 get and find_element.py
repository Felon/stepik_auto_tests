import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("http://suninjuly.github.io/wait1.html")
time.sleep(2)
button = browser.find_element(By.ID, "verify")
button.click()

message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()