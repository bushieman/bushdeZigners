from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:\Program Files\Chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

# implicit waits
driver.implicitly_wait(20)

# keys
cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver) # Actions object
actions.click(cookie)

for i in range(110):
    actions.perform()
    count = int(cookie_count.text.split(' ')[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade = ActionChains(driver)
            upgrade.move_to_element(item)
            upgrade.click()
            upgrade.perform()
