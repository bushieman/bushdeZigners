from locator import *

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def is_title_matching(self):
        return "Python" in self.driver.title

    def click_button(self):
        element = self.driver.find_element(*MainPageLocator.BUTTON)
        element.click()
