from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get('http://127.0.0.1:8080/')
install_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "installButton")))

install_button.click()