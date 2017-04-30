from selenium import webdriver
import unittest
import time
class NewVisitorTest(unittest.TestCase):

    def setUp(self):  #2
        self.browser = webdriver.Firefox()

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        self.browser.get('http://localhost:8000')
        time.sleep(7)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('WELCOME', header_text)

        searchbox = self.browser.find_element_by_id('search')
        self.assertEqual(
                searchbox.get_attribute('placeholder'),
                'Search'
        )

        #searchbox.send_keys('detective conan volume 40')

        text1 = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('total book', text1)
        text2 = self.browser.find_element_by_tag_name('p2').text
        self.assertIn('New Release Books', text2)
        text4 = self.browser.find_element_by_tag_name('p4').text
        self.assertIn('Latest Reviews', text4)
        text7 = self.browser.find_element_by_tag_name('p7').text
        self.assertIn('Top 5 Rating', text7)
        

        

        link1 = self.browser.find_element_by_link_text("Gone Girl").click()
        

        

        self.fail('Finish the test!') 
        self.browser.quit()

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
