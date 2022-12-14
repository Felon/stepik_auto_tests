import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()