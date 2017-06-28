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
        #กะทิได้ยินเกี่ยวกับ web application ที่สามารถจัดเก็บรายชื่อได้ จึงลองเข้าไปที่หน้าเว็บดังกล่าว
        self.browser.get('http://localhost:8000/')
        
        #หน้าแรกของเว็บไซต์ปรากฏแบบฟอร์มให้เข้าใช้งานและมี link สำหรับลงทะเบียน  กะทิจึงกดเข้าไปที่ link ดังกล่าว
        webapp = self.browser.find_element_by_name('webappname')
        self.assertIn('My Bookshelf', webapp.text)
        register = self.browser.find_element_by_name('register').click()
        time.sleep(2)
        
        #เมื่อเข้ามาแล้วกะทิพบกับแบบฟอร์มให้กรอกชื่อผู้ใช้งาน รหัสผ่าน และ email กะทิทำการกรอกข้อมูลทั้งหมดแล้วกดปุ่มcreate
        register = self.browser.find_element_by_name('register')
        self.assertIn('Register', register.text)
        uname = self.browser.find_element_by_name('uname')
        uname.send_keys('kati')
        password = self.browser.find_element_by_name('password')
        password.send_keys('kati123')
        email = self.browser.find_element_by_name('umail')
        email.send_keys('kati@mail.com')
        register = self.browser.find_element_by_name('submit').click()
        time.sleep(2)

        #มีข้อความปรากฏในหน้าเดิมนั้นว่า บัญชีถูกสร้างเรียบร้อยแล้ว กะทิจึงกลับไปที่หน้าลงชื่อเข้าใช้งานแล้วทำการ log in
        back_to_home = self.browser.find_element_by_name('back_to_home').click()
        time.sleep(2)
     
        webapp = self.browser.find_element_by_name('webappname')
        self.assertIn('My Bookshelf', webapp.text)

        uname = self.browser.find_element_by_name('uname')
        self.assertEqual(
                uname.get_attribute('placeholder'),
                'username'
        )
        uname.send_keys('kati')
        password = self.browser.find_element_by_name('password')
        self.assertEqual(
                password.get_attribute('placeholder'),
                'password'
        )
        password.send_keys('kati123')
        login = self.browser.find_element_by_name('submit')
        self.assertIn('LOGIN', login.text)
        login.click()
        time.sleep(2)

        #เมื่อเข้าสู่ระบบกะทิพบกับเมนูต่างๆ และข้อความ 'My Bookshelf' รวมทั้งกล่องค้นหา 

        home = self.browser.find_element_by_link_text("Home").text
        self.assertIn('Home', home)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('My Bookshelf', header_text)
        searchbox = self.browser.find_element_by_id('search')
        self.assertEqual(
                searchbox.get_attribute('placeholder'),
                'Search'
        )

        #เมื่อกวาดสายตามองดีๆกะทิพบจำนวนหนังสือทั้งหมด หัวข้อหนังสือล่าสุด  หัวข้อหนังสือที่ถูกรีวิวล่าสุด และหัวข้อหนังสือที่มีเรทคะแนนสูงสุด 
        text1 = self.browser.find_element_by_tag_name('p').text
        self.assertIn('total book', text1)
        text2 = self.browser.find_element_by_tag_name('p2').text
        self.assertIn('New Release', text2)
        text3 = self.browser.find_element_by_tag_name('p3').text
        self.assertIn('Latest Reviews', text3)
        text4 = self.browser.find_element_by_tag_name('p4').text
        self.assertIn('Top 5 Rating', text4)
        
        #เพราะเป็นครั้งแรกในการใช้งาน กะทิจึงอยากรู้ว่า web application นี้สามารถทำอะไรได้บ้างจึงเข้าไปที่เมนู about
        about = self.browser.find_element_by_link_text('About')
        self.assertIn('About', about.text)
        
        about.click()
        time.sleep(2)

        #กะทิต้องการเพิ่มหนังสือเล่มใหม่ลงใน web application จึงกดที่ Add new 
        addnew = self.browser.find_element_by_link_text('Add new')
        self.assertIn('Add new', addnew.text)
        addnew.click()
        time.sleep(5)

        title = self.browser.find_element_by_name('title')
        title.send_keys('aaa')
        author = self.browser.find_element_by_name('author')
        author.send_keys('bbb')
        time.sleep(2)
        myfile = self.browser.find_element_by_name("myfile").click()
        time.sleep(10)
        add = self.browser.find_element_by_name("ADD").click()
        time.sleep(5)
        

        #หน้าเว็บเพจเปลี่ยนกลับไปเป็นหน้าโฮม กะทิพบว่าหนังสือที่เธอเพิ่มไปนั้นปรากฏอยู่ที่ New Release เธอจึงกดเข้าไปที่หนังสือเล่มนั้น
        #กะทิพบว่าหน้าเว็บเปลี่ยนไปแสดงรายละเอียดต่างๆของหนังสือ
        
        
        book = self.browser.find_element_by_name("aaa").click()
        time.sleep(2)
        title = self.browser.find_element_by_name('title').text
        self.assertIn('aaa', title)
        author = self.browser.find_element_by_name('author').text
        self.assertIn('bbb', author)


        #และยังมีส่วนสำหรับการรีวิวหนังสืออีกด้วย กะทิจึงลองเขียนรีวิวให้หนังสือเล่มที่กำลังแสดงบนหน้าเว็บ  

        review = self.browser.find_element_by_name('review').text
        self.assertIn('REVIEW THIS BOOK', review)
        review_message = self.browser.find_element_by_name('review_message')
        review_message.send_keys('สนุก')
        time.sleep(2)

        radio_rating_n = self.browser.find_element_by_xpath(".//input[@type='radio' and @value='2']")
        radio_rating_n.click()

        radio_rating = self.browser.find_element_by_xpath(".//input[@type='radio' and @value='4']")
        radio_rating.click()

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
        
        #กะทิลองกดไปที่เมนูที่ชื่อว่า All books ซึ่งทำให้พบกับรายชื่อหนังสือทุกเล่มที่เธอมี
        allbooks = self.browser.find_element_by_link_text("All books").click()
        time.sleep(3)
        pcat = self.browser.find_element_by_name('pcat').text
        self.assertIn('My Bookshelf : Allbooks', pcat)

        #เมื่อลองกดที่ category ก็พบ droped down menu เธอจึงกดที่ Novel ทำให้พบกับรายชื่อหนังสือทุกเล่มที่เป็นประเภท Novel ที่เธอมี
        cat = self.browser.find_element_by_name("cat").click()
        time.sleep(3)
        novel = self.browser.find_element_by_name("Novel").click()
        time.sleep(3)
        pcat = self.browser.find_element_by_name('pcat').text
        self.assertIn('My Bookshelf : Novel', pcat)

        #กะทิลองค้นหาชื่อหนังสือโดยใช้ช่องค้นหา
        home = self.browser.find_element_by_link_text("Home").click()
        time.sleep(2)
        search = self.browser.find_element_by_name('search')
        search.send_keys('aaa')
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        #เมื่อเธอลองใช้งานจนพอใจแล้วจึงลงชื่อออกจากระบบ
        logout = self.browser.find_element_by_link_text('Logout').click()
        time.sleep(2)

        self.fail('Finish the test!') 
        self.browser.quit()

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
