from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from bookstore.models import Book
from bookstore.views import home, index
from django.contrib.auth.models import User 
import re

class LoginAndRegisterTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, index)  

    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    def test_login_page_returns_correct_html(self):
        request = HttpRequest()  
        response = index(request) 
        expected_html = render_to_string('bookstore/login.html')
        self.assertEqual(self.remove_csrf(response.content.decode()), expected_html)  

    def test_register_has_to_work_properly(self):
        response = self.client.post('/register/')        
        first_user = User.objects.create_user(username='kati',email='kati@mail.com',password='kati123')
        first_user.save()
        allusers = User.objects.all()
        self.assertEqual(allusers.count(), 1)

        second_user = User.objects.create_user(username='plakat',email='plakat@mail.com',password='plakat123')
        second_user.save()
        allusers = User.objects.all()
        self.assertEqual(allusers.count(), 2)

        first_user = allusers[0]
        second_user = allusers[1]
        self.assertEqual(first_user.username, 'kati')
        self.assertEqual(second_user.username, 'plakat')

    #def test_login_has_to_work_properly(self):
    #    response = self.client.post('/') 
   
#class AddNewBookTest(TestCase):

    #def test_change_to_add_page(self):
        #book_ = Book.objects.create()
        #response = self.client.get('/bookstore/newbook/')
        #self.assertTemplateUsed(response,'/bookstore/newbook.html'+'/bookstore/base.html')

    #def test_add_book(self):
    #    response = self.client.post('/B1/bookstore/newbook/',data={'title': 'A new list item','author': 'A new list item','cat':'Novel'})
        
