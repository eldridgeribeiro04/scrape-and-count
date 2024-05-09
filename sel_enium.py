from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
