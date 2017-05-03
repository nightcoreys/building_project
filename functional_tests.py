from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class NewVisitorTest(unittest.TestCase):

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        #ปิดเทอมแล้ว กะทิต้องการหาหนังสืออ่านเล่นในช่วงปิดเทอมจึงเข้าไปที่เว็บร้านหนังสือร้านหนึ่ง
        self.browser.get('http://localhost:8000')
        
        #ในหน้าโฮมจะพบข้อความ 'WELCOME' 

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('WELCOME', header_text)

        #กล่องค้นหา
        searchbox = self.browser.find_element_by_id('search')
        self.assertEqual(
                searchbox.get_attribute('placeholder'),
                'Search'
        )

        #และปรากฏจำนวนหนังสือทั้งหมด รายชื่อหนังสือล่าสุด 5 ลำดับ และรายชื่อหนังสือที่ถูกรีวิวล่าสุด 5 ลำดับ
        text1 = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('total book', text1)
        text2 = self.browser.find_element_by_tag_name('p2').text
        self.assertIn('New Release Books', text2)
        text4 = self.browser.find_element_by_tag_name('p4').text
        self.assertIn('Latest Reviews', text4)
        text7 = self.browser.find_element_by_tag_name('p7').text
        self.assertIn('Top 5 Rating', text7)
        

        #กะทิพบหนังสือที่ชื่อว่า Gone Girl เธอสนใจจึงกดที่ชื่อหนังสือเล่มนั้นซึ่งปรากฏอยู่ในรายชื่อหนังสือล่าสุด
        link1 = self.browser.find_element_by_link_text("Gone Girl").click()
        time.sleep(5)

        #หน้าเว็บเปลี่ยนไปแสดงรายละเอียดของหนังสือ ในหน้านั้นมีส่วนสำหรับรีวิว//และทำการจองหนังสือ//
        #เมื่อพบว่าผู้แต่งคือ Jo Nesbo กะทิจึงนึกได้ว่าเคยอ่านไปแล้ว เธออยากให้คนอื่นได้รู้ว่ามันสนุก จึงเขียนรีวิว 
        reviewbox = self.browser.find_element_by_name('review_message')
        reviewbox.send_keys('เยี่ยม')

        radio_rating = self.browser.find_element_by_xpath(".//input[@type='radio' and @value='4']")
        radio_rating.click()
        
        radio_rating_n = self.browser.find_element_by_xpath(".//input[@type='radio' and @value='2']")

        self.assertEqual(
                radio_rating.is_selected(),
                True
        )
        self.assertEqual(
                radio_rating_n.is_selected(),
                False
        ) 
        

        review_button = self.browser.find_element_by_name('review')
        review_button.send_keys(Keys.ENTER)       

        time.sleep(3)
#----------------------------------------------------------------------------------
        #self.browser.get('http://localhost:8000')

        #searchbox.send_keys('detective conan volume 40')
        #searchbox.send_keys(Keys.ENTER)
        #time.sleep(5)
#-----------------------------------------------------------------------
    #กะทิไม่รู้จะอ่านหนังสืออะไรจึงเข้าไปดูรีวิวทั้งหมดเพื่อช่วยในการตัดสินใจ หน้าเว็บปรากฏรายชื่อหนังสือที่ถูกรีวิวทั้งหมด กะทิพบว่า ----- เป็นหนังสือที่ถูกรีวิวเยอะ จึงกดที่ชื่อหนังสือเล่มนั้นแล้วทำการจอง
#-----------------------------------------------------------------------
    #กะทิอยากรู้ว่าหนังสือที่จองไปมีเล่มต่อทั้งหมดกี่เล่มจึงกลับไปที่หน้าโฮม แล้วทำการ search ชื่อหนังสือลงไป หน้าเว็บแสดงรายชื่อหนังสือที่มีชื่อดังกล่าว จำนวน---เล่ม เธอจึงตัดสินใจว่าถ้าอ่านเล่มนี้จบแล้วสนุก เธอจะยืมมันมาอ่านให้หมด!
#-----------------------------------------------------------------------        

        self.fail('Finish the test!') 
        self.browser.quit()

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
