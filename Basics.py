from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\Program Files\Chromedriver.exe'
driver = webdriver.Chrome(PATH)

# accessing the site
driver.get('https://techwithtim.net')
print(driver.title)

# # accessing the entire page
# print(driver.page_source)

# accessing elements
search = driver.find_element_by_name('s')
search.clear() # to clear the input field
search.send_keys('Python') # send text
search.send_keys(Keys.RETURN) # enter

# explicit waits
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'main')))
    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        dates = article.find_element_by_class_name('entry-meta')
        print(dates.text)
finally:
    driver.quit()

# driver.close() # one tab
# driver.quit() # whole browser
