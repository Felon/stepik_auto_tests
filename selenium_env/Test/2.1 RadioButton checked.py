import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    people_radio = browser.find_element(By.ID, "robotsRule") #peopleRule
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()