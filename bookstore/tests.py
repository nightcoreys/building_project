from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from bookstore.models import Book
from bookstore.views import home 

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/bookstore/home/')  
        self.assertEqual(found.func, home)  
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home(request) 
        self.assertIn(b'<h1 align=center>My Bookshelf</h1>', response.content)  
   
class AddNewBookTest(TestCase):

    #def test_change_to_add_page(self):
        #book_ = Book.objects.create()
        #response = self.client.get('/bookstore/newbook/')
        #self.assertTemplateUsed(response,'/bookstore/newbook.html'+'/bookstore/base.html')

    def test_add_book(self):
        response = self.client.post('/bookstore/newbook/',data={'title': 'A new list item','author': 'A new list item'})
        
