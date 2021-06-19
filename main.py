from selenium import webdriver
import unittest
import page

class PythonOrgSearch(unittest.TestCase):
    # setup
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files\Chromedriver.exe')
        self.driver.get('https://www.python.org/')

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matching
        
    # cleaning up
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
