from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):  #2
        self.browser = webdriver.Firefox()

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        self.browser.get('http://localhost:8000/bookstore/home')
        self.fail('Finish the test!') 


        self.browser.quit()

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
