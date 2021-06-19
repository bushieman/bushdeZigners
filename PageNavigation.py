from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

PATH = 'C:\Program Files\Chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')

link = driver.find_element_by_link_text('Python Programming')
link.click()
try:
    beginner_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials')))
    beginner_link.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sow-button-19310003')))
    button.click()
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
except:
    driver.quit()

